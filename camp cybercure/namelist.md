# Camp CyberCure: Namelist

**Challenge Type: OSINT**  
**Challenge Status: Solved**

## Challenge

Who is the mysterious leader of Camp CyberCure? This list might give a clue.

> Person 1: Same first name and last name.  
> Person 2: Same last name as a 2010 Rock and Roll Hall of Fame Inductee.  
> Person 3: Digits of their phone number add up to 61  
> Person 4: Oldest of three brothers.

One of these four suspects has only one letter 'o' in their name. Use their phone number to unzip the flag password file.

Challenge Creator: *Mark Bosco*

## Solution

1. Extract phone numbers

```py
#! /usr/bin/env python3

numbers = []

with open('suspect-list.txt') as f:
  while (line := f.readline().rstrip()):
    numbers.append(line.split(' ')[3])

with open('suspect-filtered.txt', 'a') as f:
  for n in numbers:
    f.write(n + '\n')
```

2. Crack the zip password

```bash
$ fcrackzip -u -D -p suspect-filtered.txt flag_hp.zip

PASSWORD FOUND!!!!: pw == 97475221
```

3. Extract with password

```bash
$ unzip -P 97475221 flag_hp.zip

Archive: flag_hp.zip
  extracting: flag_hp.txt
```

3. Print out flag

```bash
$ cat flag_hp.txt

NYP{0h-0h-Armadeussss}
```
