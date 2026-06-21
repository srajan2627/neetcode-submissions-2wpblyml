# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            
            # 1. Go Left
            traverse(node.left)
            
            # 2. Process Current Root Node
            result.append(node.val)
            
            # 3. Go Right
            traverse(node.right)
            
        traverse(root)
        return result