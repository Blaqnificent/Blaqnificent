# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 01:57:08 2019

@author: Bayo
"""

import sys

while True:
    print ('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print ('You typed ' + response + '.')