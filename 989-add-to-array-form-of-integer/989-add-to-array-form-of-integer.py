class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=''
        for i in range(len(num)):
            s+=str(num[i])
        m=str(int(s)+k)
        l=[]
        for i in m:
            l.append(int(i))
        return l
        
        