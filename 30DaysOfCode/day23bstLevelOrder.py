import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def __init__(self):
        self.queue = []
    def levelOrder(self,root):
        if (root == None):
            return
        self.queue.append(root)
        while(self.queue != []):
            toRemove = self.queue[0]
            print toRemove.data,
            if (toRemove.left != None):
                self.queue.append(toRemove.left)
            if (toRemove.right != None):
                self.queue.append(toRemove.right)
            self.queue.remove(toRemove)
T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)