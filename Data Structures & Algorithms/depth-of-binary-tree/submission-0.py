# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        
        def dfs(root,count):
            if root is None:
                self.ans=max(self.ans,count)
                return
            dfs(root.left,count+1)
            dfs(root.right,count+1)
        dfs(root,0)
        return self.ans
            
        