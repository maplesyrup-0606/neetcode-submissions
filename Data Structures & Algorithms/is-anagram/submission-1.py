class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False

        freq = defaultdict(int)
        freq2 = defaultdict(int)
        for i in s:
            freq[i] += 1
        
        for j in t:
            freq2[j] += 1
        
        for k in s:
            if freq[k] != freq2[k]:return False
        
        return True

