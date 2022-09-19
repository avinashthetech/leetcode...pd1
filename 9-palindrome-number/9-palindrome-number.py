class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
        
        """
        t=x
        rm=0
        while(t):
            r=t%10
            rm=rm*10+r
            t/=10
        if rm==x:
            return True
        return False"""
        

        
        