#!/bin/bash

echo "picoCTF{$(cat VaultDoorTraining.java | grep -Eo "equals\(\"(.*)\"\)" | cut -c9- | rev | cut -c3- | rev)}"