class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        unordered_map<int, int> indegree;
        
        for(const auto& edge : edges) {
            indegree[edge[1]]++;
        }
        
        vector<int> good;
        for(int i = 0; i < n; i++) {
            if (indegree.find(i) == indegree.end()) {
                good.push_back(i);
            }
        }
        
        if (good.size() == 1) {
            return good[0];
        }
        
        return -1;
    }
};
