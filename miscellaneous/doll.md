# Doll

**Challenge Type: Steganography**  
**Challenge Status: Unsolved**

## Challenge
You found an interesting Russian Doll from the factory...

## Solution

1. Extract flag file from image
```bash
$ steghide extract -sf doll.jpg

Enter passphrase: (BLANK)
```

2. Continually extract
```bash
#!/bin/bash

for i in {1..100}
do
  cat flag | base64 -d > $i.zip
  unzip -o $i.zip 
done
```

3. Enjoy

```bash
cat flag

NYP{M@try0shkA_d0!!5}
```
