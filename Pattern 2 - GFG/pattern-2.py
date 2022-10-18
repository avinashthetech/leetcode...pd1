#User function Template for python3

class Solution:
    def printTriangle(self, N):
        m=1
        while(m<=N):
            print('* '*m)
            m+=1
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends