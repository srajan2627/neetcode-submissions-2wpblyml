class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            
            elif char == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            
            elif char == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(b) - int(a))
            
            elif char == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(b)//int(a))
            
            else:
                stack.append(char)
    
        return stack.pop()
