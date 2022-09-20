class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        
        res = 0
        for p1 in points:
            m = collections.defaultdict(lambda: 0)
            for p2 in points:
                if p1 == p2: continue
                if p2[0] == p1[0]:
                    m['inf'] += 1
                    continue 
                slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                m[slope] += 1
            res = max(res, max(m.values()) + 1)        
            
        return res
        
        
        
        
        '''
        def xyz(p1,p2):
            x1,y1=p1
            x2,y2=p2
            if x1==x2:
                return 'inf'
            else:
                return (y2-y1)//(x2-x1)
        
        res=0
        n=len(points)
        if n<=2:
            return n
        for i in range(n):
            cnt=collections.defaultdict((lambda: 0))
        for j in range(i+1,n):
            slope=xyz(points[i],points[i+1])
            cnt[slope]+=1
            res=max(res,cnt[slope])     #res = max(res, max(m.values()) + 1)
        return res+1
        '''
        