# Antigravity SDE Manager without AES — By Fronsanper

**Version 1.0.0**

> A graphical utility for Linux that helps update or reinstall Antigravity on computers without AES support by using Intel SDE, while preserving the existing Antigravity configuration and Intel SDE installation.

## English (US)

### What this project does

This project provides a graphical manager for updating or reinstalling Antigravity on Linux systems whose processors do not provide AES instructions. It uses Intel SDE as a compatibility layer for the Antigravity `language_server` and is designed to preserve important local configuration while the Antigravity installation is replaced.

The manager includes:

- installation diagnostics;
- backup before replacing the Antigravity installation;
- installation/update from an official `.tar.gz` package;
- automatic detection of the Antigravity `language_server`;
- Intel SDE wrapper configuration;
- log viewing;
- backup restoration;
- a graphical Linux application launcher;
- version `1.0.0`.

### Important: what the manager preserves

The manager is designed to preserve the existing Antigravity configuration directory, when detected:

```text
~/.config/Antigravity IDE
```

It also preserves the Intel SDE installation:

```text
~/intel-sde
```

The Antigravity installation itself is updated or replaced under:

```text
/usr/share/antigravity
```

Before changing the installation, the manager creates a backup so that the existing installation can be restored when needed.

The manager does **not** intentionally delete the Antigravity configuration directory or the Intel SDE directory during the update/reinstallation process.

### Requirements

- Linux.
- Python 3.
- Tkinter (`python3-tk` on Debian/Ubuntu-based systems).
- Intel SDE installed at `~/intel-sde/sde64`.
- The official Antigravity `.tar.gz` package.
- A graphical Linux session for the manager.

### Windows

**Windows is not supported.** This project is specifically designed for Linux and uses Linux filesystem paths, permissions, application launchers, and Intel SDE Linux binaries.

### Quick start

After downloading or cloning the repository:

```bash
git clone https://github.com/Fronsanper/antigravity-sde-manager-without-aes-linux.git
cd antigravity-sde-manager-without-aes-linux
chmod +x install.sh
./install.sh
```

After installation, open **Antigravity SDE Manager without AES — By Fronsanper** from the Linux application menu. You can also run:

```bash
./run.sh
```

### Recommended workflow

1. Run the installation diagnostics.
2. Create a backup.
3. Choose **Install/Update** and select the official Antigravity `.tar.gz` package.
4. Configure the Intel SDE wrapper.
5. Launch Antigravity.

### Chats and configuration

The project does not intentionally remove `~/.config/Antigravity IDE` (or another detected configuration directory) or `~/intel-sde`. Synchronized chats should reappear after signing in with the same account, but synchronization itself is handled by Antigravity.

### Community

- Discord: [NivalityOfficial](https://discord.com/invite/z5gb4zvWsY)
- Telegram: [NivalityOfficial](https://t.me/+Ygtl-pe64d5jN2Nh)
- YouTube: [FronsanperDev](https://www.youtube.com/@FronsanperOfficial)

**By Fronsanper**

---

# Gerenciador SDE do Antigravity sem AES — Feito por Fronsanper

**Versão 1.0.0**

> Um utilitário gráfico para Linux que ajuda a atualizar ou reinstalar o Antigravity em computadores sem suporte a AES usando Intel SDE, preservando a configuração existente do Antigravity e a instalação do Intel SDE.

## Português (Brasil)

### O que este projeto faz

Este projeto fornece um gerenciador gráfico para atualizar ou reinstalar o Antigravity em sistemas Linux cujos processadores não possuem instruções AES. Ele utiliza o Intel SDE como camada de compatibilidade para o `language_server` do Antigravity e foi desenvolvido para preservar configurações locais importantes enquanto a instalação do Antigravity é substituída.

O gerenciador inclui:

- diagnóstico da instalação;
- backup antes de substituir a instalação do Antigravity;
- instalação/atualização a partir de um pacote `.tar.gz` oficial;
- detecção automática do `language_server` do Antigravity;
- configuração do wrapper Intel SDE;
- visualização de logs;
- restauração do backup;
- lançador gráfico no menu de aplicativos do Linux;
- versão `1.0.0`.

### Importante: o que o gerenciador preserva

O gerenciador foi desenvolvido para preservar o diretório de configuração existente do Antigravity, quando detectado:

```text
~/.config/Antigravity IDE
```

Ele também preserva a instalação do Intel SDE:

```text
~/intel-sde
```

A instalação do Antigravity é atualizada ou substituída em:

```text
/usr/share/antigravity
```

Antes de alterar a instalação, o gerenciador cria um backup para que a instalação existente possa ser restaurada quando necessário.

O gerenciador **não apaga deliberadamente** o diretório de configuração do Antigravity nem o diretório do Intel SDE durante o processo de atualização/reinstalação.

### Requisitos

- Linux.
- Python 3.
- Tkinter (`python3-tk` em sistemas baseados em Debian/Ubuntu).
- Intel SDE instalado em `~/intel-sde/sde64`.
- O pacote `.tar.gz` oficial do Antigravity.
- Uma sessão gráfica Linux para executar o gerenciador.

### Windows

**Windows não é suportado.** Este projeto foi desenvolvido especificamente para Linux e utiliza caminhos de sistema Linux, permissões, lançadores de aplicativos e binários Linux do Intel SDE.

### Instalação rápida

Depois de baixar ou clonar o repositório:

```bash
git clone https://github.com/Fronsanper/antigravity-sde-manager-without-aes-linux.git
cd antigravity-sde-manager-without-aes-linux
chmod +x install.sh
./install.sh
```

Depois da instalação, abra **Antigravity SDE Manager without AES — Feito por Fronsanper** pelo menu de aplicativos do Linux. Também é possível executar:

```bash
./run.sh
```

### Fluxo recomendado

1. Execute o diagnóstico da instalação.
2. Crie um backup.
3. Escolha **Instalar/Atualizar** e selecione o pacote `.tar.gz` oficial do Antigravity.
4. Configure o wrapper Intel SDE.
5. Abra o Antigravity.

### Chats e configurações

O projeto não apaga deliberadamente `~/.config/Antigravity IDE` (ou outro diretório de configuração detectado) nem `~/intel-sde`. Os chats sincronizados devem reaparecer ao entrar com a mesma conta, mas a sincronização em si é responsabilidade do próprio Antigravity.

### Comunidade

- Discord: [NivalityOfficial](https://discord.com/invite/z5gb4zvWsY)
- Telegram: [NivalityOfficial](https://t.me/+Ygtl-pe64d5jN2Nh)
- YouTube: [FronsanperDev](https://www.youtube.com/@FronsanperOfficial)

**Feito por Fronsanper**
