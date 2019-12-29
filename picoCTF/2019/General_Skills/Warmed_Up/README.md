# Warmed Up

Points: 50

## Problem
> What is 0x3D (base 16) in decimal (base 10).

## Hints
> Submit your answer in our competition's flag format. For example, if you answer was '22', you would submit 'picoCTF{22}' as the flag.

## Solution

This is just a quick conversion problem.

Using the script below, we get `picoCTF{61}` as the flag.

```python
#!/usr/bin/env python3

flag_format = "picoCTF{%d}"

print(flag_format % int(0x3D))
```

## Flag

`picoCTF{61}`