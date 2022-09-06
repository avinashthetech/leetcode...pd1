# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#pre order-->root left right
class Solution: 
    
    def __init__(self):
        self.value=0
    def getsum(self,node,ps):
        if node.left is None and node.right is None:
            self.value+=ps
        if node.left is not None:
            self.getsum(node.left,ps*10+node.left.val)
        if node.right is not None:
            self.getsum(node.right,ps*10+node.right.val)
            
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.getsum(root,root.val)
        return self.value
            
            
            
        