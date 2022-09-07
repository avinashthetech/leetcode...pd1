import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        k=dividend/divisor
        k=int(k)
        if k>pow(2,31)-1:
            return pow(2,31)-1
        else:
            return k
        if k<pow(-2,31):
            return pow(-2,31)
        else:
            return k
        