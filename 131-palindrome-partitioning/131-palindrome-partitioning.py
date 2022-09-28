class Solution:
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
    def isPal(self, s):
        return s == s[::-1]
#     def isPali(self,s,l,r):
#         while l<r:
#             if s[l]<s[r]:
#                 return False
#             l,r=l+1,r-1
#         return True
    
#     def partition(self, s: str) -> List[List[str]]:
#         res=[]
#         part=[]
        
#         def dfs(i):
#             if i>=len(s):
#                 res.append(part.copy())
#                 return 
#             for j in range(i,len(s)):
#                 if self.isPali(s,i,j):
#                     part.append(s[i:j+1])
#                     dfs(j+1)
#                     part.pop()
#         dfs(0)
#         return res
    
    
    # def isPali(self,s,l,r):
    #     while l<r:
    #         if s[l]<s[r]:
    #             return False
    #         l,r=l+1,r-1
    #     return True
            