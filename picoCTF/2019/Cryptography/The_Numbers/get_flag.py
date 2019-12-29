#!/usr/bin/env python3

flag_format = "picoCTF{%s}"

numbers = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
flag = "".join([ chr(i + 64) for i in numbers ])

print((flag_format % flag).upper())