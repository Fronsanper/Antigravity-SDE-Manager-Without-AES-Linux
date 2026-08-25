# Technical Guide

## English (US)

### Known layout

In an installation used during the preparation of this project, the binary was located at:

`/usr/share/antigravity/resources/bin/language_server`

The program searches dynamically because future versions may change this path.

### Wrapper

The wrapper executes:

```text
~/intel-sde/sde64 -skx -- language_server.real
```

It also sets `GOMAXPROCS=1` and `GODEBUG=http2client=0,tls13=0`, following the wrapper that worked in the environment used during development.

### Manual diagnostics

```bash
find /usr/share/antigravity -type f | grep language_server
file /usr/share/antigravity/resources/bin/language_server
ps -ef | grep language_server
top -p PID
tail -100 ~/antigravity-sde-wrapper.log
```

### Limitations

The manager does not control Antigravity servers, chat synchronization, or the Google account.

---

# Guia Técnico

## Português (Brasil)

### Estrutura conhecida

Em uma instalação usada durante a preparação deste projeto, o binário estava localizado em:

`/usr/share/antigravity/resources/bin/language_server`

O programa procura dinamicamente porque versões futuras podem alterar esse caminho.

### Wrapper

O wrapper executa:

```text
~/intel-sde/sde64 -skx -- language_server.real
```

Ele também define `GOMAXPROCS=1` e `GODEBUG=http2client=0,tls13=0`, seguindo o wrapper que funcionou no ambiente utilizado durante o desenvolvimento.

### Diagnóstico manual

```bash
find /usr/share/antigravity -type f | grep language_server
file /usr/share/antigravity/resources/bin/language_server
ps -ef | grep language_server
top -p PID
tail -100 ~/antigravity-sde-wrapper.log
```

### Limitações

O gerenciador não controla os servidores do Antigravity, a sincronização de chats ou a conta Google.
