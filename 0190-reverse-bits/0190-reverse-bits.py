class Solution:
    def reverseBits(self, n):
        n  = bin(n)
        rev = n[-1:1:-1]
        x = rev + (32 - len(rev))*'0'
        return int(x,2)
#         return int(bin(n)[2:].rjust(32,'0')[::-1],2)
