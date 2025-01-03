
from os import system
import subprocess

system("cd levels")
system("ls")


lol = [str(t) for t in subprocess.check_output(['ls']).split()]

print(lol[0])
for t in lol:
    print(t)