# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:49:04 2016

@author: Rahul Patni
"""

#!/bin/python

import sys

def beast(n):
    if n < 3:
        return -1
    result = ""
    if n % 3 == 0:
        result = "5" * n
        return result
    if n == 5:
        result = "3" * n
        return result
    fives = n
    threes = 0
    for i in range(n):
        fives -= 1
        threes += 1
        if fives % 3 == 0 and threes % 5 == 0:
            result = "5" * fives + "3" * threes
            return result
    return -1
    
    
def main():

    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print beast(n)

        
main()