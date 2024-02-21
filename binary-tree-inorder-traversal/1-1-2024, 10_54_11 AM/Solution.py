// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        myList = []
        getInorderTraversal(myList, root)
        return myList
        
def getInorderTraversal(myList: List[int], root: TreeNode) -> List[int]:
    if not root:
        return
    if (root.left):
        getInorderTraversal(myList, root.left)
    myList.append(root.val)
    if (root.right):
        getInorderTraversal(myList, root.right)
    return myList


        
