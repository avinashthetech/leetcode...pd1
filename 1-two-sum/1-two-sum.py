class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for id1,vl in enumerate(nums):
            
            if target-vl in d:
                return [d[target-vl],id1]
            else:
                d[vl]=id1