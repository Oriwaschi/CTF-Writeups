# Glory of the Garden

Points: 50

## Problem
> This [garden](garden.jpg) contains more than it seems. You can also find the file in /problems/glory-of-the-garden_3_346e50df4a37bcc4aa5f6e5831604e2a on the shell server.

## Hints
> What is a hex editor?

## Solution

It's usually best to only look at the hints when you're stuck. I ended up not using a hex editor at all. My usual go-to approach to inspecting image data is running some basic commands like `strings`, which extracts all strings from an image file.

When running `strings garden.jpg | tail -5` to get the last 5 strings, we get:

```
=7g&
mjx/
s\]|."Ue
\qZf
Here is a flag "picoCTF{more_than_m33ts_the_3y35a97d3bB}"
```

So the flag is `picoCTF{more_than_m33ts_the_3y35a97d3bB}`


My quick get_flag script using grep to extract only the flag:

```bash
#!/bin/bash

strings garden.jpg | grep -Eo picoCTF{.*} --color=none
```

## Flag

`picoCTF{more_than_m33ts_the_3y35a97d3bB}`