# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#2-->or
#3-->and
#1-->t
#0-->f
# post order-->left right root
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def r(n):
            if n.val==1:
                return True
            elif n.val==0:
                return False
            elif n.val==2:
                return r(n.left) or r(n.right)
            elif n.val==3:
                return r(n.left) and r(n.right)
            else:
                return False
        return r(root)
    
            
        
        