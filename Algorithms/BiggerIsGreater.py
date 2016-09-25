# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:57:53 2016

@author: Rahul Patni
"""

# BiggerIsGreater

def findBiggest(word):
    tracker = [0] * 26
    wordList= list(word)
    for w in wordList:
        val = ord(w) - ord('a')
        tracker[val] += 1
        
    result = ""
    for i in range(25, -1, -1):
        result += chr(ord('a') + i) * tracker[i]
    if result == word:
        result = "no answer"
    return result
    
    
def helper(wordList, start):
    i = start + 1
    tracker = [0] * 26
    for w in range(i, len(wordList)):
        val = ord(wordList[w]) - ord('a')
        tracker[val] += 1
    curr = i
    k = 0
    print tracker
    while k < 26:
        if tracker[k] != 0:
            wordList[curr] = chr(ord('a') + k)
            curr += 1
            tracker[k] -= 1
            if tracker[k] == 0:
                k += 1
        else:
            k += 1
    return "".join(wordList)
    
    
def findNextBiggest(word):
    wordList = list(word)
    start = len(wordList) - 1
    end = len(wordList) - 1
    for j in range(len(word) - 2, -1, -1):
        print start, j
        if ord(wordList[j + 1]) > ord(wordList[j]):
            start = j
            break
    print start
    for j in range(len(word) - 1, -1, -1):
        if ord(wordList[j]) > ord(wordList[start]):
            end = j 
            break
    print start, end
    if start > end:
        return "no answer"
    wordList[start], wordList[end] = wordList[end], wordList[start] 
    result = helper(wordList, start)
    if result != word:
        return result
    return "no answer"
    
    
def main():
    word = "dba"
    print word
    print findNextBiggest(word)
    
main()