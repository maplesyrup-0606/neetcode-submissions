class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # there will always be two numbers in the stack
        # we append till an operator comes out, compute then re-append
        # repeat till all tokens
    
        operators = "+-*/"

        stack = []
        for token in tokens:
            print(stack)
            if token not in operators:
                stack.append(int(token))
            
            else:
                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    res = first / second
                    if res > 0: res = math.floor(res)
                    else: res = math.ceil(res)
                    stack.append(res)
        
        return stack[0]
