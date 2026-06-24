# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: if the tree is completely empty
        if not root:
            return []
        
        result = []
        stack = [root]
        
        # Keep processing until there are no more nodes left in the stack
        while stack:
            # 1. Process the Root (Pop the current top node)
            curr = stack.pop()
            result.append(curr.val)
            
            # 2. Push Right child first (so it sits lower in the stack)
            if curr.right:
                stack.append(curr.right)
                
            # 3. Push Left child second (so it sits at the very top to be popped next)
            if curr.left:
                stack.append(curr.left)
                
        return result