# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertChildren(root)
        return root

    def invertChildren(self, root: Optional[TreeNode]) -> None:
        if None == root:
            return
        root.left, root.right = root.right, root.left
        self.invertChildren(root.left)
        self.invertChildren(root.right)
