# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if (not root):
            return False
        return self.pathLeafSum(root, targetSum, 0)
    
    def pathLeafSum(self, root: Optional[TreeNode], targetSum: int, currSum: int) -> bool:
        if (not root):
            return False
        if (not root.left and not root.right):
            return targetSum == currSum + root.val
        return self.pathLeafSum(root.left, targetSum, currSum + root.val) or self.pathLeafSum(root.right, targetSum, currSum + root.val)
