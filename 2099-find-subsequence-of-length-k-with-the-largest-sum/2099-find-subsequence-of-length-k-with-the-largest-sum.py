class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for num in nums:
            heapq.heappush(heap, num)
            output.append(num)
            if len(heap)>k:
                output.remove(heapq.heappop(heap))
                
        return output
                
        