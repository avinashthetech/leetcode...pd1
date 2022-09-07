class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        s=0
        for i in range(0,n):
            nums.append(start+2*i)
        
        for i in range(n):
            s^=nums[i]
        return s
            
            
        