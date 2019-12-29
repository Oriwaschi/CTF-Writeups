# 2Warm

Points: 50

## Problem
> Can you convert the number 42 (base 10) to binary (base 2)?

## Hints
> Submit your answer in our competition's flag format. For example, if you answer was '11111', you would submit 'picoCTF{11111}' as the flag.

## Solution

To solve this problem, we can either use an online decimal-to-binary converter like [this one](https://www.rapidtables.com/convert/number/decimal-to-binary.html) or we can write our own little get_flag script using Python. This is the way I actually went.

The content of get_flag.py:

```python
#!/usr/bin/env python3

flag_format = "picoCTF{%s}"

# bin(42) converts 42 to binary, but it actually returns 
# "0b101010", therefore we need to slice off the first 2
# characters, which we do with [2:]

print(flag_format % bin(42)[2:])
```

And there you go! Our flag is `picoCTF{101010}`.

## Flag

`picoCTF{101010}`