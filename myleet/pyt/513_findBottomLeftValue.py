# Definition for a binary tree node.
from classtree import *

class Solution:
    def findBottomLeftValue(self, root):
        queue = [root]

        for node in queue:
            queue += filter(None, (node.right, node.left))
        print(queue,node.val)
        return node.val

# test case
para1='[2,1,3,null,5,null,4]'
root=deserialize(para1)
drawtree(root)

Solution().findBottomLeftValue(root)

