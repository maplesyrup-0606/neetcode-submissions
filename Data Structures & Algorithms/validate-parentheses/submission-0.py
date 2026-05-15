class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        stack = deque([])

        for char in s:
            if char in mp.values():
                stack.append(char)
            
            if char in mp.keys():
                if not stack: return False
                if stack[-1] == mp[char]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False