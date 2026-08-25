# Guia técnico

## Layout conhecido

Em uma instalação usada durante a preparação deste projeto, o binário estava em:

`/usr/share/antigravity/resources/bin/language_server`

O programa procura dinamicamente porque versões futuras podem mudar esse caminho.

## Wrapper

O wrapper executa:

```text
~/intel-sde/sde64 -skx -- language_server.real
```

Também define `GOMAXPROCS=1` e `GODEBUG=http2client=0,tls13=0`, seguindo o wrapper que funcionou no ambiente usado.

## Diagnóstico manual

```bash
find /usr/share/antigravity -type f | grep language_server
file /usr/share/antigravity/resources/bin/language_server
ps -ef | grep language_server
top -p PID
tail -100 ~/antigravity-sde-wrapper.log
```

## Limitações

O gerenciador não controla os servidores do Antigravity, a sincronização de chats ou a conta Google.
