class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function constrainedSubsetSum($nums, $k) {
        $dp = $nums;
        $q = [];
        array_push($q, 0);
        for ($i = 1; $i < count($nums); $i++) {
            while (end($q) < $i - $k) {
                array_pop($q);
            }
            $dp[$i] = max($dp[$i], $dp[end($q)] + $nums[$i]);
            while (count($q) > 0 && $dp[$q[0]] <= $dp[$i]) {
                array_shift($q);
            }
            array_unshift($q, $i);
        }
        return max($dp);
    }
}