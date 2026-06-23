class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # if a new character pops out we split


        res = []

        freq = Counter(s)
        n = len(s)

        prev = 0
        visited = set()
        
        for i in range(n):
            curr = s[i]
            freq[curr] -= 1
            visited.add(curr)
        
            if freq[curr] == 0:
                meh = False
                for seen in visited:
                    if freq[seen] != 0:
                        meh = True
                        break
                
                if not meh:
                    res.append(i - prev + 1)
                    # print(prev, i)
                    prev = i + 1
                    visited = set()
            
                
        
        return res