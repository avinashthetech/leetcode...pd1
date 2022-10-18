class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(a,i,j):
            while(i<j):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j-=1
        def swap(nums,i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        n=len(nums)
        t=-1
        i=n-1
        k=0
        while i>=1:
            if nums[i]>nums[i-1]:
                t=i-1
                break
            i-=1
        if t==-1:
            reverse(nums,0,n-1)
            return
        mn=nums[t]
        for i in range(t+1,n):
            if nums[i]>mn:
                mn=min(mn,nums[i])
                k=i

        swap(nums,t,k)
        reverse(nums,t+1,n-1)
        
        """
        Do not return anything, modify nums in-place instead.
        """
        