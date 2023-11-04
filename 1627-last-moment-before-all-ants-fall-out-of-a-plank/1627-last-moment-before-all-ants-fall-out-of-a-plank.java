class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        int t = 0;
        if (left.length > 0) {
            t = Arrays.stream(left).max().getAsInt();
        }
        if (right.length > 0) {
            t = Math.max(t, n - Arrays.stream(right).min().getAsInt());
        }
        return t;
    }
}
