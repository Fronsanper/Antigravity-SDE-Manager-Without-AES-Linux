# Guia para leigos

## O que este programa resolve?

Ele ajuda a instalar uma versão nova do Antigravity sem apagar sua configuração e seu Intel SDE.

## Passo 1 — instalar o gerenciador

Na pasta extraída do ZIP:

```bash
chmod +x install.sh
./install.sh
```

Depois procure **Antigravity SDE Manager without AES — Linux** no menu do Linux.

## Passo 2 — diagnóstico

Clique em **Diagnóstico**. Ele mostra se a instalação, configuração e SDE existem e onde o `language_server` foi encontrado.

## Passo 3 — backup

Clique em **Fazer Backup** antes de instalar uma versão nova. O backup da instalação fica em `/usr/share/antigravity.bak` ou em um nome com data se já existir um backup.

## Passo 4 — atualizar

Clique em **Instalar / Atualizar**, selecione o `.tar.gz` baixado do site oficial e confirme. O programa valida a estrutura antes de substituir a instalação.

## Passo 5 — Intel SDE

Clique em **Configurar Intel SDE**. O programa localiza o `language_server`, salva o binário real como `language_server.real` e coloca um wrapper que chama `~/intel-sde/sde64 -skx`.

## Passo 6 — testar

Clique em **Abrir Antigravity**. Se pedir login, use a mesma conta.

## Timeout de 60 segundos

Se aparecer `Timeout: language server did not report its port within 60s`, clique em Diagnóstico e confira:

```bash
tail -100 ~/antigravity-sde-wrapper.log
ps -ef | grep language_server
```

## Erro de AES

Se aparecer `compiled with aes enabled`, confira se o wrapper está sendo usado e se `~/intel-sde/sde64` existe.

## Restaurar

Use **Restaurar Backup**. Isso restaura a instalação do programa; não remove `~/.config/Antigravity IDE` (ou outro diretório de configuração detectado) nem `~/intel-sde`.

## Importante

Nunca compartilhe senhas, tokens, cookies ou logs que contenham dados privados.
