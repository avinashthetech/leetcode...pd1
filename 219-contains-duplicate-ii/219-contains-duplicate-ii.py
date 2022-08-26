class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l={}
        for i,n in enumerate(nums):
            if n in l:
                if(i-l[n])<=k:
                    return True
            l[n]=i

            
            
        return False 
