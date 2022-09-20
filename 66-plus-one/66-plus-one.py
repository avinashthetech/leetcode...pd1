class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        l=[]
        s=" "
        for i in range(len(digits)):
            s+=str(digits[i])
        m=str(int(s)+1)
        for i in m:
            l.append(i)
        return l
            
        
        
        