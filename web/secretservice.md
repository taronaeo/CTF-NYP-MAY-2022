# Secret Service

**Challenge Type: security.txt**
**Challenge Status: Unsolved**

## Challenge
You received a text file from an EdOverflow and Yakok Shafranovich. What is inside? Does it come from other survivors?  
https://secret.nypinfsecctf.tk

## Solution
1. Google about the collaboration between EdOverflow and Yakok Shafranovich

It should return https://datatracker.ietf.org/doc/html/draft-foudil-securitytxt or https://datatracker.ietf.org/doc/html/rfc9116.

2. What to do

RFC9116 states that a security.txt file is to be placed in the //:{{website}}/.well-known folder.

3. Get the security.txt contents

```bash
$ curl https://secret.nypinfsecctf.tk/.well-known/security.txt

Contact: mailto:ilovetehpengctf@gmail.com
Expires: 2023-12-31T15:59:00.000Z
```

4. Email the contact

They should return an out-of-office reply.
```
ilove tehpeng
14:41 (3 hours ago)
to Aaron Teo

Dear Agent,

I will be out of office to find the secret vaccine at [REDACTED] Location.
NYP{s3curiTy_d0t_tXT}
Regards,
Agent Teh
```
