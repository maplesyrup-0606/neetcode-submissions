class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        base = 0
        for i in range(31):
            residual = n % 2
            res += residual
            res = res << 1
            n = n >> 1
        return res + n % 2