class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();
        int start = -1;
        int end = -1;

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                start = mid;
                right = mid;
            } else if (nums[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left = 0;
        right = nums.size();

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                end = mid;
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return {start, end};
    }
};
