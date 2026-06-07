class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mp = {
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "0":0
        }

        def make_int(s):
            base = 1
            res = 0
            for i in range(len(s) - 1, -1, -1):
                res += mp[s[i]] * base
                base *= 10
            
            return res
        
        return str(make_int(num1) * make_int(num2))