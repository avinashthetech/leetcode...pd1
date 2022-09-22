class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        
        
        if n!=0:
            i=0
            while m<len(nums1):
                nums1[m]=nums2[i]
                m+=1
                i+=1
        nums1.sort()
        
        
        
        
        """"
        if n != 0:
            i = 0
            while m < len(nums1):
                nums1[m] = nums2[i]
                i += 1
                m += 1
        
        nums1.sort()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        i=0
        j=0
        l=[]
        for i in range(m):
            if nums1[i]<nums2[j]:
                l.append(nums1[i])
        
            else:
                l.append(nums2[j])
                j+=1
                if j>n:
                    break;
        print(l)
    
       
        1-->1
        1-->1
        2-->1,2-->2,0
        Do not return anything, modify nums1 in-place instead.
        """
        