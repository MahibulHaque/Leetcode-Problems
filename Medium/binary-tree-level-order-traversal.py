# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        queue = [];
        res=[]
        queue.append(root);
        
        while(len(queue) > 0):
            elemList=[]
            count = len(queue);

            for i in range(0,count):
                node = queue.pop(0);
                elemList.append(node.val)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
                
            res.append(elemList)
        return res;