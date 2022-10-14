class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        me=set()
        
        
        for i in arr:
            if 2*i in me or i/2 in me:
                return True
            me.add(i)
        return False
        