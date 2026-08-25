#!/usr/bin/env python3
import json, os, shutil, subprocess, tarfile, tempfile
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

V = '1.0.0'
BRAND = 'By Fronsanper'
HOME = Path.home()
AG = Path('/usr/share/antigravity')
LINK = Path('/usr/bin/antigravity')
SDE = HOME / 'intel-sde' / 'sde64'
LOG = HOME / 'antigravity-sde-wrapper.log'
CONFIGS = [HOME/'.config/Antigravity', HOME/'.config/antigravity', HOME/'.config/Antigravity IDE']
MANAGER_DIR = HOME / '.config' / 'antigravity-sde-manager'
BACKUP_DIR = MANAGER_DIR / 'backups'
STATE_FILE = MANAGER_DIR / 'state.json'

T = {
'pt-BR': {
'lang':'Português (Brasil)','en':'English (US)','setup':'Setup Wizard','welcome':'Bem-vindo ao Antigravity SDE Manager without AES — Linux!','next':'Próximo','finish':'Concluir','cancel':'Cancelar',
'title':'Antigravity SDE Manager without AES — Linux','subtitle':'v1.0.0 • By Fronsanper','diag':'🔎 Diagnóstico','backup':'💾 Backup agora','install':'📦 Instalar / Atualizar','already':'✅ Já tenho o Antigravity instalado','sde':'⚙ Aplicar Intel SDE','uninstall':'🗑 Desinstalar SDE / restaurar original','restore':'♻ Restaurar instalação original','settings':'🌐 Idioma','log':'📜 Ver Log','launch':'🚀 Abrir Antigravity',
'mode':'Como você quer começar?','mode_inst':'Já tenho o Antigravity instalado','mode_tar':'Tenho um .tar.gz para instalar/atualizar','langpick':'Escolha o idioma do programa','confirm_backup':'Antes de alterar o Antigravity, será feito backup automático da instalação e do settings.json quando disponível. Continuar?','confirm_sde':'Antes de aplicar o Intel SDE, o language_server original será salvo automaticamente para que possa ser restaurado na desinstalação. Continuar?','confirm_uninstall':'Remover a integração do Intel SDE e restaurar o language_server e o settings.json originais salvos pelo gerenciador?','confirm_restore':'Restaurar a instalação original salva pelo gerenciador?','ok':'OK','error':'Erro','done':'Concluído','notfound':'Não encontrado','choose':'Selecionar arquivo','no_tar':'Nenhum .tar.gz encontrado nas pastas comuns. Escolha um arquivo manualmente.','found':'Instaladores encontrados automaticamente:','nop':'Não encontrado','sdeok':'Intel SDE detectado','not_sde':'Intel SDE não encontrado em ~/intel-sde/sde64.','already':'Instalação existente detectada.','saved':'Backup salvo em','restored':'Original restaurado com sucesso.','uninstalled':'Integração SDE removida; original restaurado.','sde_done':'Integração Intel SDE configurada.','settings_restored':'settings.json original restaurado quando disponível.'},
'en-US': {
'lang':'Português (Brasil)','en':'English (US)','setup':'Setup Wizard','welcome':'Welcome to Antigravity SDE Manager without AES — Linux!','next':'Next','finish':'Finish','cancel':'Cancel',
'title':'Antigravity SDE Manager without AES — Linux','subtitle':'v1.0.0 • By Fronsanper','diag':'🔎 Diagnostics','backup':'💾 Backup now','install':'📦 Install / Update','already':'✅ I already have Antigravity installed','sde':'⚙ Apply Intel SDE','uninstall':'🗑 Uninstall SDE / restore original','restore':'♻ Restore original installation','settings':'🌐 Language','log':'📜 View Log','launch':'🚀 Open Antigravity',
'mode':'How do you want to start?','mode_inst':'I already have Antigravity installed','mode_tar':'I have a .tar.gz to install/update','langpick':'Choose the application language','confirm_backup':'Before changing Antigravity, an automatic backup of the installation and settings.json (when available) will be created. Continue?','confirm_sde':'Before applying Intel SDE, the original language_server will be saved automatically so it can be restored when uninstalling. Continue?','confirm_uninstall':'Remove the Intel SDE integration and restore the original language_server and settings.json saved by the manager?','confirm_restore':'Restore the original installation saved by the manager?','ok':'OK','error':'Error','done':'Done','notfound':'Not found','choose':'Select file','no_tar':'No .tar.gz was found in common folders. Choose a file manually.','found':'Installers automatically found:','nop':'Not found','sdeok':'Intel SDE detected','not_sde':'Intel SDE not found at ~/intel-sde/sde64.','already':'Existing installation detected.','saved':'Backup saved to','restored':'Original restored successfully.','uninstalled':'SDE integration removed; original restored.','sde_done':'Intel SDE integration configured.','settings_restored':'Original settings.json restored when available.'}
}

def state():
    MANAGER_DIR.mkdir(parents=True, exist_ok=True); BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    try: return json.loads(STATE_FILE.read_text(encoding='utf-8'))
    except Exception: return {'language':'pt-BR','setup_done':False,'install_backup':'','language_backup':'','settings_backups':[]}

def save(s):
    MANAGER_DIR.mkdir(parents=True, exist_ok=True); STATE_FILE.write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')

def run_root(script):
    p = subprocess.run(['pkexec','bash','-c',script], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if p.returncode != 0: raise RuntimeError(p.stdout.strip() or 'Operação administrativa falhou.')
    return p.stdout

def settings_files():
    out=[]
    for d in CONFIGS:
        p=d/'User'/'settings.json'
        if p.exists(): out.append(p)
        p=d/'settings.json'
        if p.exists(): out.append(p)
    return out

def find_ls():
    if not AG.exists(): return []
    return sorted(p for p in AG.rglob('language_server') if p.is_file())

def find_tarballs():
    roots=[HOME/'Downloads', HOME/'Documents', HOME/'Desktop']
    out=[]
    for r in roots:
        if r.exists(): out += list(r.glob('*.tar.gz')) + list(r.glob('*.tgz'))
    return sorted({p.resolve() for p in out}, key=lambda p:p.stat().st_mtime, reverse=True)

def make_install_backup(s):
    if not AG.exists(): return None
    dest=BACKUP_DIR/'antigravity-original'
    if dest.exists():
        i=1
        while (BACKUP_DIR/f'antigravity-original-{i}').exists(): i+=1
        dest=BACKUP_DIR/f'antigravity-original-{i}'
    run_root(f'cp -a {AG!s} {dest!s}')
    s['install_backup']=str(dest); save(s); return dest

def backup_settings(s):
    backups=[]
    for src in settings_files():
        dst=BACKUP_DIR / f'settings-{len(backups)+1}.json.original'
        shutil.copy2(src,dst); backups.append({'src':str(src),'backup':str(dst)})
    s['settings_backups']=backups; save(s); return backups

def restore_settings(s):
    restored=0
    for item in s.get('settings_backups',[]):
        b=Path(item.get('backup','')); src=Path(item.get('src',''))
        if b.exists():
            src.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(b,src); restored+=1
    return restored

def locate_bundle(root):
    for p in root.rglob('antigravity'):
        if p.is_file() and (p.parent/'resources').is_dir(): return p.parent
    raise RuntimeError('O arquivo não contém uma instalação válida do Antigravity.')

def install_tar(path,s):
    if not path: return
    path=Path(path)
    if not path.exists(): raise RuntimeError('Arquivo não encontrado.')
    if not messagebox.askyesno(I18N('title',s), I18N('confirm_backup',s)): return
    make_install_backup(s); backup_settings(s)
    with tempfile.TemporaryDirectory(prefix='ag-sde-') as td:
        with tarfile.open(path,'r:*') as tar: tar.extractall(td)
        bundle=locate_bundle(Path(td))
        run_root(f"set -e; rm -rf {AG!s}; cp -a {bundle!s} {AG!s}; ln -sfn {AG/'antigravity'!s} {LINK!s}")

def apply_sde(s):
    if not SDE.exists(): raise RuntimeError(I18N('not_sde',s))
    targets=find_ls()
    if not targets: raise RuntimeError('language_server não encontrado.')
    target=next((p for p in targets if p.name=='language_server'),targets[0])
    backup=BACKUP_DIR/'language_server.original'
    if not backup.exists(): run_root(f'cp -a {target!s} {backup!s}')
    real=target.with_name('language_server.real')
    if not real.exists(): run_root(f'mv {target!s} {real!s}')
    wrapper='''#!/usr/bin/env bash\nSDE_BIN="$HOME/intel-sde/sde64"\nDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"\nif [ ! -x "$SDE_BIN" ]; then echo "Intel SDE not found: $SDE_BIN" >&2; exit 127; fi\nexport GOMAXPROCS=1\nexport GODEBUG=http2client=0,tls13=0\nexec "$SDE_BIN" -skx -- "$DIR/language_server.real" "$@" >> "$HOME/antigravity-sde-wrapper.log" 2>&1\n'''
    with tempfile.NamedTemporaryFile('w',delete=False) as f: f.write(wrapper); tmp=f.name
    try: run_root(f'cp {tmp!s} {target!s}; chmod +x {target!s}')
    finally: os.unlink(tmp)

def uninstall_sde(s):
    backup=BACKUP_DIR/'language_server.original'
    targets=find_ls(); target=next((p for p in targets if p.name=='language_server'),None)
    if not backup.exists(): raise RuntimeError('Backup original do language_server não encontrado.')
    if target is None: target=AG/'resources/bin/language_server'
    real=target.with_name('language_server.real')
    run_root(f'cp -a {backup!s} {target!s}; chmod +x {target!s}; rm -f {real!s}')
    restore_settings(s)

def restore_install(s):
    b=Path(s.get('install_backup',''))
    if not b.exists():
        choices=sorted(BACKUP_DIR.glob('antigravity-original*'),key=lambda p:p.stat().st_mtime,reverse=True)
        if not choices: raise RuntimeError('Nenhum backup da instalação foi encontrado.')
        b=choices[0]
    run_root(f"set -e; rm -rf {AG!s}; cp -a {b!s} {AG!s}; ln -sfn {AG/'antigravity'!s} {LINK!s}")
    restore_settings(s)

def I18N(key,s): return T[s['language']].get(key,key)

def diag_text(s):
    lines=[f"Antigravity SDE Manager without AES — Linux v{V}",BRAND,'',f"/usr/share/antigravity: {'OK' if AG.exists() else I18N('notfound',s)}",f"/usr/bin/antigravity: {'OK' if LINK.exists() else I18N('notfound',s)}",f"Intel SDE: {'OK' if SDE.exists() else I18N('notfound',s)}",'', 'language_server:']
    lines += ['  '+str(p) for p in find_ls()] or ['  nenhum']
    lines += ['', 'settings.json:'] + ['  '+str(p) for p in settings_files()] or ['  nenhum']
    return '\n'.join(lines)

class Wizard(tk.Toplevel):
    def __init__(self,app):
        super().__init__(app); self.app=app; self.s=app.s; self.lang=tk.StringVar(value=self.s.get('language','pt-BR')); self.mode=tk.StringVar(value='installed'); self.page=0
        self.title('Setup Wizard'); self.geometry('680x430'); self.resizable(False,False); self.transient(app); self.grab_set(); self.build(); self.render()
    def build(self):
        self.box=ttk.Frame(self,padding=30); self.box.pack(fill='both',expand=True); self.titlelab=ttk.Label(self.box,font=('Sans',21,'bold')); self.titlelab.pack(anchor='w',pady=(0,18)); self.content=ttk.Frame(self.box); self.content.pack(fill='both',expand=True); foot=ttk.Frame(self.box); foot.pack(fill='x',pady=(15,0)); self.back=ttk.Button(foot,command=self.go_back); self.back.pack(side='left'); self.cancel=ttk.Button(foot,command=self.destroy); self.cancel.pack(side='right'); self.next=ttk.Button(foot,command=self.go_next); self.next.pack(side='right',padx=8)
    def clear(self):
        for w in self.content.winfo_children(): w.destroy()
    def render(self):
        self.clear(); lang=self.lang.get(); t=T[lang]
        if self.page==0:
            self.titlelab.config(text=t['langpick']); ttk.Radiobutton(self.content,text=t['lang'],variable=self.lang,value='pt-BR').pack(anchor='w',pady=16); ttk.Radiobutton(self.content,text=t['en'],variable=self.lang,value='en-US').pack(anchor='w',pady=16); self.back.state(['disabled']); self.next.config(text=t['next'])
        else:
            self.titlelab.config(text=t['mode']); ttk.Radiobutton(self.content,text=t['mode_inst'],variable=self.mode,value='installed').pack(anchor='w',pady=16); ttk.Radiobutton(self.content,text=t['mode_tar'],variable=self.mode,value='tar').pack(anchor='w',pady=16); self.back.state(['!disabled']); self.next.config(text=t['finish'])
        self.cancel.config(text=t['cancel'])
    def go_back(self): self.page=0; self.render()
    def go_next(self):
        if self.page==0: self.s['language']=self.lang.get(); save(self.s); self.page=1; self.render()
        else:
            self.s['setup_done']=True; save(self.s); self.app.refresh(); self.destroy(); self.app.after(100,self.app.after_setup)

class App(tk.Tk):
    def __init__(self):
        super().__init__(); self.s=state(); self.title(f'Antigravity SDE Manager without AES — Linux v{V}'); self.geometry('980x700'); self.minsize(860,620); st=ttk.Style(self); st.theme_use('clam'); st.configure('TButton',font=('Sans',11),padding=10); st.configure('Title.TLabel',background='#101218',foreground='white',font=('Sans',24,'bold')); st.configure('Sub.TLabel',background='#101218',foreground='#aab1c0',font=('Sans',11)); self.configure(bg='#101218'); self.build(); self.refresh(); self.after(250,self.maybe_wizard)
    def tx(self,k): return T[self.s['language']][k]
    def build(self):
        h=ttk.Frame(self,padding=24); h.pack(fill='x'); self.head=ttk.Label(h,style='Title.TLabel'); self.head.pack(anchor='w'); self.sub=ttk.Label(h,style='Sub.TLabel'); self.sub.pack(anchor='w')
        b=ttk.Frame(self,padding=(24,0,24,24)); b.pack(fill='both',expand=True); l=ttk.Frame(b); l.pack(side='left',fill='y',padx=(0,18)); r=ttk.Frame(b); r.pack(side='left',fill='both',expand=True)
        self.bs={}
        keys=['diag','backup','install','already','sde','uninstall','restore','log','launch','settings']
        for k in keys:
            self.bs[k]=ttk.Button(l,command=lambda k=k:self.handle(k),width=31); self.bs[k].pack(fill='x',pady=4)
        self.out=tk.Text(r,bg='#171a22',fg='#e7eaf0',insertbackground='white',relief='flat',font=('DejaVu Sans Mono',10),wrap='word'); self.out.pack(fill='both',expand=True)
    def refresh(self):
        self.head.config(text=self.tx('title')); self.sub.config(text=self.tx('subtitle')); [self.bs[k].config(text=self.tx(k)) for k in self.bs]
    def show(self,x): self.out.delete('1.0','end'); self.out.insert('end',x); self.out.see('end')
    def maybe_wizard(self):
        if not self.s.get('setup_done'): Wizard(self)
    def after_setup(self):
        self.refresh(); self.show(self.tx('welcome'))
    def confirm(self,k): return messagebox.askyesno(self.tx('title'),self.tx(k))
    def handle(self,k):
        try:
            if k=='diag': self.show(diag_text(self.s))
            elif k=='backup': self.action_backup()
            elif k=='install': self.action_install()
            elif k=='already': self.show(self.tx('already')+'\n\n'+diag_text(self.s))
            elif k=='sde': self.action_sde()
            elif k=='uninstall': self.action_uninstall()
            elif k=='restore': self.action_restore()
            elif k=='log': self.show(LOG.read_text(errors='replace')[-50000:] if LOG.exists() else self.tx('notfound'))
            elif k=='launch': subprocess.Popen(['antigravity']); self.show('Antigravity started.')
            elif k=='settings': self.change_language()
        except Exception as e: self.show('ERRO / ERROR:\n\n'+str(e)); messagebox.showerror(self.tx('error'),str(e))
    def action_backup(self):
        if not self.confirm('confirm_backup'): return
        p=make_install_backup(self.s); backup_settings(self.s); self.show(f"{self.tx('saved')}: {p or 'nenhum'}")
    def action_install(self):
        cands=find_tarballs(); initial=str(cands[0].parent) if cands else str(HOME/'Downloads');
        if cands: self.show(self.tx('found')+'\n'+'\n'.join('• '+str(p) for p in cands))
        else: self.show(self.tx('no_tar'))
        p=filedialog.askopenfilename(title=self.tx('choose'),initialdir=initial,filetypes=[('Antigravity','*.tar.gz *.tgz'),('All files','*.*')])
        if p: install_tar(p,self.s); self.show(self.tx('done'))
    def action_sde(self):
        if not self.confirm('confirm_sde'): return
        backup_settings(self.s); apply_sde(self.s); self.show(self.tx('sde_done'))
    def action_uninstall(self):
        if not self.confirm('confirm_uninstall'): return
        uninstall_sde(self.s); self.show(self.tx('uninstalled')+'\n'+self.tx('settings_restored'))
    def action_restore(self):
        if not self.confirm('confirm_restore'): return
        restore_install(self.s); self.show(self.tx('restored'))
    def change_language(self):
        val=messagebox.askyesno('Language','Use English (US)?')
        self.s['language']='en-US' if val else 'pt-BR'; save(self.s); self.refresh()

if __name__=='__main__': App().mainloop()
