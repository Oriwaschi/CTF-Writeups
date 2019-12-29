# vault-door-training

Points: 50

## Problem
> Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](VaultDoorTraining.java)

## Hints
> The password is revealed in the program's source code.

## Solution

Examining the given `VaultDoorTraining.java`, we can immediately see the flag:

```java
// The password is below. Is it safe to put the password in the source code?
// What if somebody stole our source code? Then they would know what our
// password is. Hmm... I will think of some ways to improve the security
// on the other doors.
//
// -Minion #9567
public boolean checkPassword(String password) {
    return password.equals("w4rm1ng_Up_w1tH_jAv4_fcb79c48f5b");
}
```

An automated way of getting the flag in Bash:

```bash
#!/bin/bash

echo "picoCTF{$(cat VaultDoorTraining.java | grep -Eo "equals\(\"(.*)\"\)" | cut -c9- | rev | cut -c3- | rev)}"
```

Inserting the password in our flag format gives us the flag:
`picoCTF{w4rm1ng_Up_w1tH_jAv4_fcb79c48f5b}`

## Flag

`picoCTF{w4rm1ng_Up_w1tH_jAv4_fcb79c48f5b}`