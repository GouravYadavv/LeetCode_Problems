public class Solution {
    public int NumFactoredBinaryTrees(int[] arr) {
        Array.Sort(arr);
        Dictionary<int, long> dp = new Dictionary<int, long>();

        foreach (int i in arr) {
            dp[i] = 1;

            foreach (int j in arr) {
                if (i % j == 0 && dp.ContainsKey(i / j)) {
                    dp[i] += dp[j] * dp[i / j];
                }
            }
        }

        long result = 0;
        foreach (var val in dp.Values) {
            result += val;
        }

        return (int)(result % (Math.Pow(10, 9) + 7));
    }
}