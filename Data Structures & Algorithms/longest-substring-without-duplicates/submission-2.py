class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0
        ret = 1
        
        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            j = i + 1

            while j < len(s):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                j += 1
            ret = max(ret, j - i)
        return ret