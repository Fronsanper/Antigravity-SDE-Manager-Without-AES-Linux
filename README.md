# Antigravity SDE Manager without AES — Linux

**Versão 1.0.0**

Gerenciador gráfico para Linux que ajuda a atualizar/reinstalar o Antigravity em computadores sem AES, usando Intel SDE.

## Objetivo

Preservar `~/.config/Antigravity IDE` (ou outro diretório de configuração detectado) e `~/intel-sde` enquanto a instalação em `/usr/share/antigravity` é atualizada. O programa faz backup antes de trocar a instalação.

## Recursos

- Diagnóstico da instalação.
- Backup.
- Instalação/atualização a partir de `.tar.gz`.
- Detecção do `language_server`.
- Configuração do wrapper Intel SDE.
- Visualização do log.
- Restauração do backup.
- Lançador gráfico no menu do Linux.

## Requisitos

Linux, Python 3, Tkinter (`python3-tk`), Intel SDE em `~/intel-sde/sde64` e o `.tar.gz` oficial do Antigravity.

## Uso

```bash
chmod +x install.sh
./install.sh
```

Depois abra **Antigravity SDE Manager without AES — Linux** pelo menu de aplicativos. Também é possível executar `./run.sh`.

### Fluxo recomendado

1. Diagnóstico.
2. Backup.
3. Instalar/Atualizar e selecionar o `.tar.gz`.
4. Configurar Intel SDE.
5. Abrir Antigravity.

## Chats e configurações

O projeto não apaga deliberadamente `~/.config/Antigravity IDE` (ou outro diretório de configuração detectado) nem `~/intel-sde`. Chats sincronizados devem reaparecer ao entrar com a mesma conta, mas a sincronização é responsabilidade do próprio Antigravity.

## GitHub

```bash
git init
git add .
git commit -m "Antigravity SDE Manager without AES — Linux 1.0.0"
```

Crie um repositório vazio no GitHub e use o endereço fornecido pelo GitHub para `git remote add origin` e `git push`. Não publique tokens, cookies, logs pessoais, configurações ou arquivos do Antigravity.
