class Solution:
    
    
    '''
    8 4 2 1
     11 -->3   1010
     01-->1    1011-->or-->1011-->and-->1010-->xor-->0001
--> 100   10101
    '''
    def addBinary(self, a: str, b: str) -> str:
        
        def od(a):
            n=len(a)
            s=0
            for i in range(len(a)):
                s+=pow(2,i)*int(a[n-i-1])
            return s
    
        c=od(a)+od(b)
        p=bin(c)[2:]
        return p                        
                                
                                
       
        