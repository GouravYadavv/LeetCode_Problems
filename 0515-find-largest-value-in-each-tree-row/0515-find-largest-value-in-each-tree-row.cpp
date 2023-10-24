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
    vector<int> largestValues(TreeNode* root) {
        if (!root) {
            return {};
        }

        vector<int> res;
        stack<pair<TreeNode*, int>> s;
        s.push({root, 0});

        while (!s.empty()) {
            TreeNode* node = s.top().first;
            int level = s.top().second;
            s.pop();

            if (level == res.size()) {
                res.push_back(node->val);
            } else {
                res[level] = max(res[level], node->val);
            }

            if (node->left) {
                s.push({node->left, level + 1});
            }
            if (node->right) {
                s.push({node->right, level + 1});
            }
        }

        return res;
    }
    };