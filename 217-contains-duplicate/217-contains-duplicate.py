class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for i in c:
            if c[i]>1:
                return True
        return False
        