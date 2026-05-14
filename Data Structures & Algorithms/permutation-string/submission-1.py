class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1) : return False
        
        w = len(s1)
        s1_sorted = sorted(s1)
        for i in range(len(s2) - w + 1):
            sub_s2 = s2[i : i + w]

            print(sub_s2)
            if sorted(sub_s2) == s1_sorted: 
                return True
    
        return False
