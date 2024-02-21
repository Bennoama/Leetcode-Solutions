// https://leetcode.com/problems/balanced-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int Max(int a, int b){
    return a > b ? a : b;
}

int Height(struct TreeNode* root){
    if (!root)
    {
        return 0;
    }
    return 1 + Max(Height(root->left), Height(root->right));
}

bool CheckIfDIffIsAtMostOne(int a, int b)
{
    return a == b + 1 || b == a + 1 || a == b;
}

bool isBalanced(struct TreeNode* root){
    if (!root){
        return true;
    }

    int rightH = Height(root->right);
    int leftH = Height(root->left);
    return CheckIfDIffIsAtMostOne(rightH, leftH) && isBalanced(root->left) && isBalanced(root->right);
    }