# ElfVirus

**Challenge Type: String in Binary**
**Challenge Status: Solved**

## Challenge
We have succesfully infiltrated the headquarter of the virus company, and managed to steal an important file

## Solution

```bash
$ strings file | grep -o "NYP{.*}"

NYP{0xLoA4hkyKonseT2}
```
