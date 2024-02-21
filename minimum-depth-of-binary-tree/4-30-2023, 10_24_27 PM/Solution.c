// https://leetcode.com/problems/minimum-depth-of-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int Min(int a, int b)
{
  return (a < b ? a : b);
}

int minDepth(struct TreeNode* root){
  if (!root)
  {
    return 0;
  }
  if (!root->left){
    return 1 + minDepth(root->right);
  }
  if (!root->right){
    return 1 + minDepth(root->left);

  }
  return 1 + Min(minDepth(root->left), minDepth(root->right));
}