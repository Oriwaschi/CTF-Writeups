# The Numbers

Points: 50

## Problem
> The [numbers](the_numbers.png)... what do they mean?

## Hints
> The flag is in the format PICOCTF{}

## Solution

Looking at the tiny range of numbers (1 - 21), this looks a lot like characters displayed by their place in the alphabet.
Knowing the flag format being `picoCTF{...}`, we only need to care about the part between the curly braces.

A quick Python script does the trick:

```python
#!/usr/bin/env python3

flag_format = "picoCTF{%s}"

numbers = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
flag = "".join([ chr(i + 64) for i in numbers ])

print((flag_format % flag).upper())
```

## Flag

`PICOCTF{THENUMBERSMASON}`