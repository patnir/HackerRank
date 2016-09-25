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
        print start, end
        if ord(wordList[end]) > ord(wordList[j]):
            start = j
            wordList[start], wordList[end] = wordList[end], wordList[start]
            return helper(wordList, start)
        if ord(wordList[end]) < ord(wordList[j]) and ord(wordList[end]) < ord(wordList[0]):
            start = j
            end = j
    return "no answer"
    
    
def main():
    word = "dkhc"
    print word
    print findNextBiggest(word)
    
main()