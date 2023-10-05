class Solution {
    fun majorityElement(nums: IntArray): List<Int> {
        val dict = mutableMapOf<Int, Int>()
        for (i in nums) {
            if (dict.containsKey(i)) {
                dict[i] = dict[i]!! + 1
            } else {
                dict[i] = 1
            }
        }

        val res = mutableListOf<Int>()
        val compare = nums.size / 3
        for ((key, value) in dict) {
            if (value > compare) {
                res.add(key)
            }
        }

        return res
    }
}