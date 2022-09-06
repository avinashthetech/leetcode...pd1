"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
        post order-->left right root
        1--> 3 2 4
        3-->5,6    2-->None    4-->None
        5-->None
        6-->None
        st-->5,6,2,4,1
        
        
        st=[]
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ds=[]
        def postpd(root):
            if root is not None:
                for p in root.children:
                    postpd(p)
                    ds.append(p.val)
        postpd(root)
        if root:
            ds.append(root.val)
        return ds
    """         
        ans=[]
        def post(root):
            if root:
                for x in root.children:
                    post(x)
                    ans.append(x.val)
        post(root)
        if root:
            ans.append(root.val)
        return ans"""