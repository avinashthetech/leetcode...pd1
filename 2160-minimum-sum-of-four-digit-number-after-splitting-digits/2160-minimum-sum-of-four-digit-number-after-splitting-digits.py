class Solution:
    def minimumSum(self, num: int) :
        n=sorted(str(num))
        return int(n[0]+n[3])+int(n[1]+n[2])
            
        
        
        