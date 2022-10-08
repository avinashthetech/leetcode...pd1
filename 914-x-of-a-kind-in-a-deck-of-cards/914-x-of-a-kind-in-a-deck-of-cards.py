class Solution:

    def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        n = len(deck)
        if n == 1:
            return 0
        dic = {}
        for ele in deck:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        g = dic[ele]
        se = set(dic.values())
        for ele in se:
            g = gcd(max(g,ele),min(g,ele))

        return 1 if g>1 else 0