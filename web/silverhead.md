# Silver Head

**Challenge Type: Robots Exclusion Standard (SEO)**

## Challenge
Congrats! You managed to reach here. Now you have to activate the self-destruct system. Only Silver Head know what the password is. The only information you know about Silver Head is that it is not a living human...

http://silver.nypinfsecctf.tk

## Solution

1. Check robots.txt
```bash
$ curl --no-progress-meter https://silver.nypinfsecctf.tk/robots.txt
User-Agent: *
Disallow: /NYPCTFflag.html
```

2. Get the disallowed page
```bash
$ curl --no-progress-meter https://silver.nypinfsecctf.tk/NYPCTFflag.html | grep -i "NYP{.*}"
<h1>NYP{danger!this_action_is_irreversible}</h1>
```
