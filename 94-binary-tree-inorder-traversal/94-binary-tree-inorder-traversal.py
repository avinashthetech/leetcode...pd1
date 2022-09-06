# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#inoder...---> left root right....root is print the val of node
#st=[]
#ds=[4,2,5,1,6,3,7]
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        ds=[]
        while root is not None or st!=[]:
            while root is not None:
                st.append(root)
                root=root.left
            root=st.pop()
            ds.append(root.val)
            root=root.right
        return ds
        
        
        
        """
        ds=[]
      
        if root is None:
            return ds
        return self.inorderTraversal(root.left)+ [root.val]+self.inorderTraversal(root.right)
       
        if root is None:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
            """
        
        
        