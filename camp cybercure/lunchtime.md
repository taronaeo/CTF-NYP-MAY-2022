# Camp CyberCure: Lunch Time

## Challenge
Before you can enter Camp CyberCure, you should bring some food. Luckily, one of your friends knows a place.

This restaurant is located less than 1000m from Jurong East MRT.

Use the postal code of the building to unzip the folder and get your flag.

Credits: Image from Google Street View.

Challenge Creator: *Mark Bosco*

## Solution

1. Generate SG Postal Codes

```py
#! /usr/bin/env python3

with open('codes.txt', 'a') as file:
  for code in range(999999 + 1):
    file.write(str(code).rjust(6, '0') + '\n')
```

2. Crack the zip password

```bash
$ fcrackzip -u -D -p codes.txt flag_restaurant.zip

PASSWORD FOUND!!!!: pw == 609079
```

3. Extract with password

```bash
$ unzip -P 609079 flag_restaurant.zip

Archive: flag_restaurant.zip
  extracting: flag_restaurant.txt
```

4. Print out flag

```bash
$ cat flag_restaurant.txt

NYP{S0m3_g00d_f00d_on_THE_WAY}

Your reward: VpFD79ASAh
```
