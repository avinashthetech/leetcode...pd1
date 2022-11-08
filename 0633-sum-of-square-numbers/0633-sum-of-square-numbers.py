class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l=0
        h=int(sqrt(c))
        while l<=h:
            m=l**2+h**2
            if m==c:
                return True
            elif m>c:
                h-=1
            else:
                l+=1
        return False
        