#User function Template for python3
class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, k) :

        t,m,d=0,0,dict()

        for i in range(n):

            t+=arr[i]

            if(t%k==0):

                m=max(m,i+1)

            if(t%k in d):

                m=max(m,i-d[t%k])

            else:

                d[t%k]=i

        return m
    # 	def longSubarrWthSumDivByK (self,arr,  n, K) :
	    
# 	    t,m.d=0,0,dict()
# 	    for i in range(n):
# 	        t+=arr[i]
# 	        if(t%k==0):
# 	            m=max(m,i+1)
# 	        if(t%k in d):
# 	            m=max(m,i-d[t%k])
# 	        else:
# 	            d[t%k]=i
# 	    return m
	    
		#Complete the function




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends