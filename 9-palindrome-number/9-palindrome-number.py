class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] 
        
        
      
    """"    t=x
        rm=0
        while(t):
            r=t%10
            rm=r+rm*10
            t=t//10
        return rm==x
       """
        

        
        