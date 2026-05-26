class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mp = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        res = []
        level = deque([""])
        for digit in digits:
            chars = mp[digit]

            n = len(level)
            for i in range(n):
                node = level.popleft()
                for char in chars:
                    level.append(node + char)
        
        return list(level)