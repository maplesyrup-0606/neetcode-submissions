class Solution:
    # naiive: between strings pre/app-end strings (e.g. <neet>)
    def encode(self, strs: List[str]) -> str:
        ret = "<neet>"
        for string in strs:
            ret += string + "<neet>"
        # print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        x = len("<neet>")
        for i in range(len(s) - x):
            if s[i : i + x] == "<neet>":
                j = i + x
                while j < len(s) - x and s[j : j + x] != "<neet>":
                    j += 1
                if j - i == x: ret.append("") 
                else: ret.append(s[i + x : j])
        return ret

