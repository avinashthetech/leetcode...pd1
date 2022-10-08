class Solution:
    def isHappy(self, n: int) -> bool:
        
        while (n != 1) and (n != 4):
            s=0
            while n:
                r=n%10
                s+=r*r
                n//=10
            n=s
        return n==1
                
                
        
        
        
        
        