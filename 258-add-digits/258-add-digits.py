class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            total = 0
            while num:
                total += num%10
                num //= 10
            num = total
        return num
        
#         def solve(num):
#             s=0
#             while(num):
#                 r=num%10
#                 s+=r
#                 num//=10
#             if s<=9:
#                 return s
#             else:
#                 solve(s)
        
#         print(solve(num))
        
        
     
        