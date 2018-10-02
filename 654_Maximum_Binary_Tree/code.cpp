/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
    if (nums.size() == 0) {
        return nullptr;
    } else if (nums.size() == 1) {
        TreeNode* root = new TreeNode(nums[0]);
        return root;
    } else if (nums.size() == 2) {
        if (nums[0] > nums[1]) {
            TreeNode* root = new TreeNode(nums[0]);
            TreeNode* right = new TreeNode(nums[1]);
            root->right = right;
            return root;
        } else {
            TreeNode* root = new TreeNode(nums[1]);
            TreeNode* left = new TreeNode(nums[0]);
            root->left = left;
            return root;
        }
    } else {
        vector<int>::iterator res = std::max_element(nums.begin(), nums.end());

        int max = *res;
        TreeNode* root = new TreeNode(max);

        vector<int> leftTree;
        leftTree.assign(nums.begin(), res);
        root->left = constructMaximumBinaryTree(leftTree);

        vector<int> rightTree;
        rightTree.assign(res + 1, nums.end());
        root->right = constructMaximumBinaryTree(rightTree);

        return root;
    }
}
};