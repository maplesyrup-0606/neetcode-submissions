class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        j = 0
        while True:
            if n == 1:
                return True
            
            if n in visited:
                return False
            
            visited.add(n)

            x = 0
            while n > 0:
                x += (n % 10) ** 2
                n = n // 10
            n = x
            # print(n)
            # j += 1
            # if j == 10:
            #     break
            # print(n)

        return False