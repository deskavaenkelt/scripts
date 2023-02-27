# Linux

## Links

- [tail](https://www.linuxfoundation.org/blog/blog/classic-sysadmin-14-tail-and-head-commands-in-linux-unix#:~:text=Linux%20Tail%20Command%20Syntax&text=Tail%20is%20a%20command%20which,of%20a%20file%2C%20then%20exits.)
- [less](https://linuxize.com/post/less-command-in-linux/)

## Logs

Apt logs

```bash
tail -f /var/log/apt/term.log
```

```bash
less +F /var/log/apt/term.log
less +F /var/log/messages
less +N /var/log/messages   # show line numbers
less +X /var/log/messages   # leave file contents on screen, use the -X option:
```

When launched with +F, less will behave pretty much the same as `tail -f`.
