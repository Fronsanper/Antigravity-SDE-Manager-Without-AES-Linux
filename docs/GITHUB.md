# Publicar no GitHub

O pacote já é estruturado como um repositório.

```bash
git init
git add .
git commit -m "Antigravity SDE Manager without AES — Linux 1.0.0"
```

Crie no GitHub um repositório vazio, por exemplo `Antigravity-SDE-Manager`. Depois use o comando de `git remote add origin` mostrado pelo GitHub e faça `git push -u origin main`.

Para uma release:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Não envie `.config`, logs, tokens, cookies, senhas, chaves privadas, instaladores proprietários ou seu diretório Intel SDE.
