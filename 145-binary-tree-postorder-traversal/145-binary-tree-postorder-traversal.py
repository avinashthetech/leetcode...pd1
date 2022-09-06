# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#post --> left right root 
"""

             3
        2         4
    1       5  0      6

st=[3,2,1]
ds=[]


"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        ds=[]
        while root or st:
            while root :

                st.append(root)
                root=root.left
            
            temp=st[-1].right
            if temp:
                root=temp
            else:
                temp=st.pop()
                ds.append(temp.val)
                while st and temp==st[-1].right:
                    temp=st.pop()
                    ds.append(temp.val)
                    
        return ds
                
            
        
        
        
        """
        if root is None:
            return []
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
        
        """