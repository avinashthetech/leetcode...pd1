class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1=set(nums)
        if len(nums1)==len(nums):
            return False
        return True
        """
        c=Counter(nums)
        for i in c:
            if c[i]>1:
                return True
        return False
        """