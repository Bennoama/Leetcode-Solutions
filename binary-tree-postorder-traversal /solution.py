# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if None == root:
            return []
        newList = list()
        self.traverse(root, newList)
        return newList

    def traverse(self, root:Optional[TreeNode], currList: List[int]) -> None:
        if (None == root):
            return
        self.traverse(root.left, currList)
        self.traverse(root.right, currList)
        currList.append(root.val)
