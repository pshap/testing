#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 13:00:36 2018

@author: PeterShapiro

"""

from random import randint
player = input('Rock(r), paper (p), or scissors(s)?')
abbrmatch = {'r':'Rock','p':'Paper', 's':'Scissors'}
valid = ('r', 'p', 's')
if player not in valid:
    print('YOU LOSE!')
    raise Exception('you idiot')
print(abbrmatch[player], 'vs', end=' ')
chosen = randint(1,3)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'
print(str.lower(abbrmatch[computer]))

compwin = 'Computer wins!'
playwin = 'Player wins!'

if player == computer:
    print('Draw!')
elif player == 'r' and computer == 's':
    print(playwin)
elif player == 'r' and computer == 'p':
    print(compwin)
elif player == 'p' and computer == 'r':
    print(playwin)
elif player == 'p' and computer == 's':
    print(compwin)
elif player == 's' and computer == 'r':
    print(compwin)
elif player == 's' and computer == 'r':
    print(playwin)
