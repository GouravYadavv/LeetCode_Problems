class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Map<Integer, Integer> dict = new HashMap<>();
        for (int i : nums) {
            dict.put(i, dict.getOrDefault(i, 0) + 1);
        }
        
        List<Integer> res = new ArrayList<>();
        int compare = nums.length / 3;
        for (Map.Entry<Integer, Integer> entry : dict.entrySet()) {
            if (entry.getValue() > compare) {
                res.add(entry.getKey());
            }
        }
        
        return res;
    }
}