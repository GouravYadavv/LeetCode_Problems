public class Solution {
    public int MaximumScore(int[] nums, int k) {
        int res = nums[k];
        int i = k;
        int j = k;
        int min_val = nums[k];

        while (i > 0 || j < nums.Length - 1) {
            if (i == 0) {
                j += 1;
                min_val = Math.Min(min_val, nums[j]);
            } else if (j == nums.Length - 1) {
                i -= 1;
                min_val = Math.Min(min_val, nums[i]);
            } else if (nums[i - 1] > nums[j + 1]) {
                i -= 1;
                min_val = Math.Min(min_val, nums[i]);
            } else {
                j += 1;
                min_val = Math.Min(min_val, nums[j]);
            }

            res = Math.Max(res, min_val * (j - i + 1));
        }

        return res;
    }
}
