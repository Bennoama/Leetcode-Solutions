// https://leetcode.com/problems/sum-of-left-leaves

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    int sumLeft(TreeNode* root, bool isLeft) {
        if (!root) {
            return 0;
        }
        if (root->left || root->right) {
            return sumLeft(root->left, true) + sumLeft(root->right, false);
        }
        return isLeft ? root->val : 0;
    }
    int sumOfLeftLeaves(TreeNode* root) {
        if (!root) {
            return 0;
        }
        return sumLeft(root->left, true) + sumLeft(root->right, false);
    }
};