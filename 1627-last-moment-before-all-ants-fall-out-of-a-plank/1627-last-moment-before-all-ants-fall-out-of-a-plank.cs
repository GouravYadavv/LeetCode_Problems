public class Solution {
    public int GetLastMoment(int n, int[] left, int[] right) {
        int t = 0;
        if (left.Length > 0) {
            t = left.Max();
        }
        if (right.Length > 0) {
            t = Math.Max(t, n - right.Min());
        }
        return t;
    }
}
