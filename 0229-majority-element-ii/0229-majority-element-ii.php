class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function majorityElement($nums) {
        $dict = [];
        foreach ($nums as $i) {
            if (isset($dict[$i])) {
                $dict[$i]++;
            } else {
                $dict[$i] = 1;
            }
        }

        $res = [];
        $compare = count($nums) / 3;
        foreach ($dict as $key => $value) {
            if ($value > $compare) {
                $res[] = $key;
            }
        }

        return $res;
    }
    }