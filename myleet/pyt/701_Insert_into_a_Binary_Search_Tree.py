# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from classtree import *
import random

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        x,y=root,None

        #find y=right place to insert
        while x:
            y = x
            if val < x.val:
                x = x.left
            else:
                x = x.right

        # if y not exist, blank tree, insert to root
        if y == None:
            return TreeNode(val)
        elif val < y.val:
            y.left=TreeNode(val)
        else:
            y.right=TreeNode(val)

        # print(root)
        return root

    def insertIntoBST2(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)

        if not root:
            return new_node

        curr = root
        while True:
            if curr.val > val:
                if not curr.left:
                    curr.left = new_node
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    break
                else:
                    curr = curr.right
        return root


    def insertIntoBST3(self, root, val):
        if(root == None): return TreeNode(val);
        if(root.val < val): root.right = self.insertIntoBST(root.right, val);
        else: root.left = self.insertIntoBST(root.left, val);
        return(root)

astr=''
ali=list(range(1,80))
random.shuffle(ali)
for i in ali:
    if len(astr)==0:
        astr += str(i)
    else:
        astr += (',' + str(i))

random.shuffle(ali)
print(ali)

para3='['+astr+']'
print(para3)

para1='[4,2,7,1,3]'
root=deserialize(para3)
Solution().insertIntoBST3(root,81)

drawtree(root)


