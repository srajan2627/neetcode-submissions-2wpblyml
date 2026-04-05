class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr = 0

        for char in tokens:
            if char == "+":
                while stack:
                    curr += stack[-1]
                    stack.pop()
            
            elif char == "*":
                while stack: 
                    curr *= stack[-1]
                    stack.pop()
            
            elif char == "-":
                while stack:
                    curr -= stack[-1]
                    stack.pop()
            
            elif char == "/":
                while stack: 
                    curr /= stack[-1]
                    stack.pop()
            
            else:
                stack.append(int(char))
            
        return curr

