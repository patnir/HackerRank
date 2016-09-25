# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:15:20 2016

@author: Rahul Patni
"""

"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def helper(head):
    if head == None:
        return None
    ret = helper(head.next)
    if ret == None:
        return head
    curr = head
    curr.next = None
    rCurr = ret
    while (rCurr.next != None):
        rCurr = rCurr.next
    rCurr.next = curr
    return ret
    

def Reverse(head):
    ret = helper(head)
    head = ret
    return head