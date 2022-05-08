# Script Kiddies

## Challenge
To find out more about the vaccine that the Pentagon has developed, you decide to hack their website. It is not necessary to be an IT expert to hack a website. Important: please do not hack the actual Pentagon website.

https://scriptkiddie.nypinfsecctf.tk/

## Solution
**Run this in Chrome Debug Console**

```js
> document.getElementById("coolkid").innerHTML = "scriptkiddie"
< 'scriptkiddie'

> omega()
< undefined

> document.getElementById("skript").innerHTML
< 'NYP{J4V4SCR1PT_K1DD13}'
```
