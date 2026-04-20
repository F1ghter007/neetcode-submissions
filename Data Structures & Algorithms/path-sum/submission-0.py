# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def issum(self,root,targetsum,tempsum):
        if not root:
            return False
        tempsum+=root.val
        if not root.left and not root.right and tempsum==targetsum:
            return True
        if self.issum(root.left,targetsum,tempsum):
            return True
        if self.issum(root.right,targetsum,tempsum):
            return True
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.issum(root,targetSum,0)
        

        
        

        