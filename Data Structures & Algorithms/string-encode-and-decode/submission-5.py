import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for idx, word in enumerate(strs):
            res += f"[{idx}]" + word

        return res
    def decode(self, s: str) -> List[str]:
        indices = []
        res = []
        for m in re.finditer(r"\[\d+\]", s):
            indices.append((m.start(), m.end()))

        for idx, pair in enumerate(indices):
            if idx == len(indices) - 1:
                res.append(s[pair[1]:])
            else:
                second_pair = indices[idx + 1]
                res.append(s[pair[1]:second_pair[0]])
            
        return res