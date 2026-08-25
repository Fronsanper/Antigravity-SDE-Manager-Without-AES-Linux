# User Guide

## English (US)

### What does this program solve?

It helps install a new version of Antigravity without removing your existing configuration or Intel SDE installation.

### Step 1 — Install the manager

In the extracted ZIP folder:

```bash
chmod +x install.sh
./install.sh
```

Then look for **Antigravity SDE Manager without AES — By Fronsanper** in the Linux application menu.

### Step 2 — Diagnostics

Click **Diagnostics**. It shows whether the installation, configuration, and SDE exist and where the `language_server` was found.

### Step 3 — Backup

Click **Create Backup** before installing a new version. The installation backup is stored at `/usr/share/antigravity.bak` or under a timestamped name if a backup already exists.

### Step 4 — Update

Click **Install / Update**, select the `.tar.gz` downloaded from the official website, and confirm. The program validates the package structure before replacing the installation.

### Step 5 — Intel SDE

Click **Configure Intel SDE**. The program locates the `language_server`, saves the real binary as `language_server.real`, and places a wrapper that calls `~/intel-sde/sde64 -skx`.

### Step 6 — Test

Click **Open Antigravity**. If login is requested, use the same account.

### 60-second timeout

If `Timeout: language server did not report its port within 60s` appears, click **Diagnostics** and check:

```bash
tail -100 ~/antigravity-sde-wrapper.log
ps -ef | grep language_server
```

### AES error

If `compiled with aes enabled` appears, check whether the wrapper is being used and whether `~/intel-sde/sde64` exists.

### Restore

Use **Restore Backup**. This restores the application installation; it does not remove `~/.config/Antigravity IDE` (or another detected configuration directory) or `~/intel-sde`.

### Important

Never share passwords, tokens, cookies, or logs containing private data.

---

# Guia do Usuário

## Português (Brasil)

### O que este programa resolve?

Ele ajuda a instalar uma nova versão do Antigravity sem remover sua configuração existente ou a instalação do Intel SDE.

### Passo 1 — Instalar o gerenciador

Na pasta extraída do ZIP:

```bash
chmod +x install.sh
./install.sh
```

Depois procure **Antigravity SDE Manager without AES — Feito por Fronsanper** no menu de aplicativos do Linux.

### Passo 2 — Diagnóstico

Clique em **Diagnóstico**. Ele mostra se a instalação, a configuração e o SDE existem e onde o `language_server` foi encontrado.

### Passo 3 — Backup

Clique em **Fazer Backup** antes de instalar uma nova versão. O backup da instalação fica em `/usr/share/antigravity.bak` ou em um nome com data se já existir um backup.

### Passo 4 — Atualizar

Clique em **Instalar / Atualizar**, selecione o `.tar.gz` baixado do site oficial e confirme. O programa valida a estrutura do pacote antes de substituir a instalação.

### Passo 5 — Intel SDE

Clique em **Configurar Intel SDE**. O programa localiza o `language_server`, salva o binário real como `language_server.real` e coloca um wrapper que chama `~/intel-sde/sde64 -skx`.

### Passo 6 — Testar

Clique em **Abrir Antigravity**. Se pedir login, use a mesma conta.

### Timeout de 60 segundos

Se aparecer `Timeout: language server did not report its port within 60s`, clique em **Diagnóstico** e confira:

```bash
tail -100 ~/antigravity-sde-wrapper.log
ps -ef | grep language_server
```

### Erro de AES

Se aparecer `compiled with aes enabled`, confira se o wrapper está sendo usado e se `~/intel-sde/sde64` existe.

### Restaurar

Use **Restaurar Backup**. Isso restaura a instalação do programa; não remove `~/.config/Antigravity IDE` (ou outro diretório de configuração detectado) nem `~/intel-sde`.

### Importante

Nunca compartilhe senhas, tokens, cookies ou logs que contenham dados privados.
