# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.sumBSTInRange(root, low, high, 0)

    def sumBSTInRange(self, root: Optional[TreeNode], low: int, high: int, currSum: int) -> int:
        if not root:
            return 0
        addition = root.val if root.val <= high and root.val >= low else 0
        return addition + self.sumBSTInRange(root.left, low, high, currSum) + self.sumBSTInRange(root.right, low, high, currSum)
