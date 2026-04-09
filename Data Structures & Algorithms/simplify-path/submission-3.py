class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        stack = []

        for i in s:
            if i == '..':
                if stack:
                    stack.pop()
            elif i != "" and i != ".":
                stack.append(i)
        
        return "/" + "/".join(stack)
