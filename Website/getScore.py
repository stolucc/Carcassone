#!/usr/bin/env python3

# Get updated scores of all players
from cgitb import enable 
enable()

from getGameController import *
print('Content-Type: text/plain')
print()

gC = getGamecontroller()
scores = []
for i in range(3):
    scores += [gC._players[i]._score]
print(scores)
setGameController(gC)
