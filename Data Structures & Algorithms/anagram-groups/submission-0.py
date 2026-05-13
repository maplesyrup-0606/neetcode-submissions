class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            res[''.join(sorted(string))].append(string)

        ret = []
        for k, v in res.items():
            ret.append(v)
        
        return ret
