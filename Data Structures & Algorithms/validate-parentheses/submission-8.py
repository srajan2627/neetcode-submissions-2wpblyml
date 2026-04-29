class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = { '[':']',
                        '{':'}',
                        '(':')'}

        p_stack = []

        for char in s:
            if char in parantheses.keys():
                p_stack.append(char)
            else:
                if not p_stack:
                    return False
                p_open = p_stack.pop()
                if char != parantheses[p_open]:
                    return False
        
        if not p_stack:
            return True
            