// https://leetcode.com/problems/deepest-leaves-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        treeHeight = self.findHeight(root)
        return self.getSumOfDeepestLeaves(root, treeHeight, 1)

    def findHeight(self, root: Optional[TreeNode]) -> int:
        if (None == root):
            return 0
        if (None == root.left and None == root.right):
            return 1
        return 1 + max(self.findHeight(root.left), self.findHeight(root.right))

    def getSumOfDeepestLeaves(self, root:Optional[TreeNode], treeHeight:int, currentHeight:int) -> int:
        if (None == root):
            return 0
        if (currentHeight == treeHeight):
            return root.val
        return self.getSumOfDeepestLeaves(root.left, treeHeight, currentHeight + 1) + \
               self.getSumOfDeepestLeaves(root.right, treeHeight, currentHeight + 1)