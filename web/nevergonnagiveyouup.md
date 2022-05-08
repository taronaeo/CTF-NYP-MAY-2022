# Never Gonna Give You Up

## Challenge
You have been walking for a few hours. Zombies are everywhere. Are you the only survivor now? Should you give up?

http://giveup.nypinfsecctf.tk

## Solution
```bash
$ curl --no-progress-meter https://giveup.nypinfsecctf.tk/flag.html | grep -i "NYP{.*}"
<!-- NYP{r1ck_r0ll3d} -->
```
