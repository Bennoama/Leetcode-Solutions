// https://leetcode.com/problems/symmetric-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool areTreesSymmetric(struct TreeNode* root1, struct TreeNode* root2)
{
    if ((root1 == NULL && root2 != NULL) || (root2 == NULL && root1 != NULL))
    {
        return false;
    }
    if (root1 == NULL && root2 == NULL)
    {
        return true;
    }
    return ((root1->val == root2->val && areTreesSymmetric(root1->left, root2->right)
    && areTreesSymmetric(root1->right, root2->left)));
}

bool isSymmetric(struct TreeNode* root){
    return areTreesSymmetric(root->left, root->right);
}

