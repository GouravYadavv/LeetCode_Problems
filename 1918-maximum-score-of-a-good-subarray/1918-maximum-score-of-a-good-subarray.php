class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumScore($nums, $k) {
        $es = $nums[$k];
    $i = $k;
    $j = $k;
    $min_val = $nums[$k];
    $len = count($nums);
    $res = $min_val * ($j - $i + 1);

    while ($i > 0 || $j < $len - 1) {
        if ($i == 0) {
            $j += 1;
            $min_val = min($min_val, $nums[$j]);
        } elseif ($j == $len - 1) {
            $i -= 1;
            $min_val = min($min_val, $nums[$i]);
        } elseif ($nums[$i - 1] > $nums[$j + 1]) {
            $i -= 1;
            $min_val = min($min_val, $nums[$i]);
        } else {
            $j += 1;
            $min_val = min($min_val, $nums[$j]);
        }

        $res = max($res, $min_val * ($j - $i + 1));
    }

    return $res;
    }
}