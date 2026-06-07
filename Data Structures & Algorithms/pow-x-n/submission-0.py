class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1

        i = 1
        if n < 0: 
            x = 1 / x
            n = -n
        
        base = x
        while i < n:
            x *= base
            i += 1
        
        return x