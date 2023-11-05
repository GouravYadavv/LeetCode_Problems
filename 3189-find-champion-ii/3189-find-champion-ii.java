import java.util.*;

class Solution {
    public int findChampion(int n, int[][] edges) {
        Map<Integer, Integer> indegree = new HashMap<>();
        
        for (int[] edge : edges) {
            int endNode = edge[1];
            indegree.put(endNode, indegree.getOrDefault(endNode, 0) + 1);
        }
        
        List<Integer> good = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!indegree.containsKey(i)) {
                good.add(i);
            }
        }
        
        if (good.size() == 1) {
            return good.get(0);
        }
        
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        int n = 5;
        int[][] edges = {{0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 0}};
        int ret = new Solution().findChampion(n, edges);
        System.out.println(ret); // Output: -1
    }
}
