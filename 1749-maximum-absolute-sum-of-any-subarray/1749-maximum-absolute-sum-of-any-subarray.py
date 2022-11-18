class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
#         mixc=nums[0]
#         cmix=nums[0]
        
#         maxc=nums[0]
#         cmax=maxc
#         for i in range(1,len(nums)):
#             cmax=max(nums[i],cmax+nums[i])
#             maxc=max(cmax,maxc)
#         for i in range(1,len(nums)):
#             cmix=max(nums[i],cmix+nums[i])
#             mixc=max(cmix,mixc)
            
#         return max(abs(maxc),abs(mixc))
        
        
        
        min_sum = nums[0]
        curr_min = nums[0]
        
        max_sum = nums[0]
        curr_max = max_sum
        
        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(curr_max, max_sum)
        
        for i in range(1, len(nums)):
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(curr_min, min_sum)
        
        return max(abs(max_sum), abs(min_sum))