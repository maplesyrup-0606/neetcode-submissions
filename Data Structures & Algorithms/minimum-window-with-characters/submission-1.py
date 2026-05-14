class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        t_freq = Counter(t)
        t_len = len(t)
        ret = ""
        for w_len in range(t_len, len(s) + 1):
            s_sub = s[0 : w_len]
            s_sub_freq = Counter(s_sub)
            for i in range(len(s) - w_len + 1):
                s_sub = s[i : i + w_len]
                p = True

                # print(t_freq, s_sub_freq)
                for k, v in t_freq.items():
                    if k not in s_sub_freq:
                        p = False
                        break
                    
                    if v > s_sub_freq[k]:
                        p = False
                        break
                
                if p :
                    return s_sub


                if i + w_len < len(s):
                    curr_char = s[i]
                    next_char = s[i + w_len]

                    s_sub_freq[curr_char] -= 1
                    if s_sub_freq[curr_char] == 0:
                        del s_sub_freq[curr_char]
                    
                    if next_char not in s_sub_freq:
                        s_sub_freq[next_char] = 0
                    s_sub_freq[next_char] += 1

        return ""