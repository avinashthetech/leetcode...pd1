
import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p=[]
      
        for i in nums1:
            p.append(i)
        for i in nums2:
            p.append(i)
        
        a=statistics.median(p)
        return a
            
        