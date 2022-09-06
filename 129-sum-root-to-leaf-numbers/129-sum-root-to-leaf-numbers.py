# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#pre order-->root left right
class Solution:
    def __init__(self):
        self.value = 0
    
    def getSums(self,node,path_sum):
            
            if node.left is None and node.right is None: # found a leaf
                self.value += path_sum
            
            if node.left is not None: # update left child sum 
                self.getSums(node.left,path_sum*10+node.left.val)
            
            if node.right is not None: # update right child sum
                self.getSums(node.right,path_sum*10+node.right.val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.getSums(root,root.val)
        return self.value
            
            
            
        