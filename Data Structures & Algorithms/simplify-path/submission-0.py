class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        print(s)
        stack = []
        simpath = ""

        for i in s:
            if i == '':
                continue
            elif i == '..':
                stack.pop()
            else:
                stack.append(i)
        
        return "/".join(stack)
