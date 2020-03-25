# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 01:24:03 2019

@author: Bayo
"""

while True:
    print ('Who are you?')
    name = input()
    if name != 'Bayo':
        continue
    print ('Hello, Bayo. What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted!')