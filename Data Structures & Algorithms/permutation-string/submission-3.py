class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1) : return False
        
        w = len(s1)
        s1_freq = Counter(s1)
        for i in range(len(s2) - w + 1):
            sub_s2_freq = Counter(s2[i : i + w])

            if s1_freq == sub_s2_freq:
                return True
    
        return False
