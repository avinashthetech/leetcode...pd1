class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        
        
        
        nums=set(nums)
        
        
        while original in nums:
            original*=2
        return original
        
#         cnt=original
#         for i in nums:
#             if i%original==0:
                
#                 for original in nums:
#                     cnt*=2
             
#         return cnt
            
        
        
        
#         pd=set()
        
#         for i in nums:
#             if original in pd or original==i:
#                 original*=2
#             pd.add(i)
#         return original
                
               
#         for i in nums:
#             if original==i:
#                 original*=2
#         return original
        