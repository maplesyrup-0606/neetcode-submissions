class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        """
            For each step we either add:
                1. opening
                2. closing
            
            When we open - add num open by 1 
            When we close - reduce num open by 1
        """

        open = "("
        close = ")"
        
        self.res = []
        def dfs(num_open, n, so_far):
            if num_open == 0 and n == 0:
                self.res.append(so_far)
            if n < 0:
                return
            if num_open < 0:
                return
            
            dfs(num_open + 1, n - 1, so_far + "(")
            dfs(num_open - 1, n, so_far + ")")
        
        dfs(0, n, "")

        return self.res