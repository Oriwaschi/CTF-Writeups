# Lets Warm Up

Points: 50

## Problem
> If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## Hints
> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

## Solution

To get the flag, we can either use an online hex-to-decimal converter like [this one](https://www.rapidtables.com/convert/number/hex-to-decimal.html) or we can write our own little script.

The content of get_flag.py:

```python
#!/usr/bin/env python3

flag_format = "picoCTF{%s}"

print(flag_format % chr(0x70))
```

## Flag

`picoCTF{p}`