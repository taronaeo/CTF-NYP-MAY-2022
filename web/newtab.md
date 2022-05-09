# New Tab

**Challenge Type: Inspect Element**  
**Challenge Status: Solved**

## Challenge
You want to try if you can connect to the network during the zombie outbreak. You open a new tab and notice something strange.

http://newtab.nypinfsecctf.tk

## Solution

```bash
$ curl --no-progress-meter https://newtab.nypinfsecctf.tk | grep -i "NYP{.*}"
FLAG NYP{INSPECT_ELEMENT@}
```
