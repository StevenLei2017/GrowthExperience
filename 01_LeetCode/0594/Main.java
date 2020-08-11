import java.util.Map;
import java.util.TreeMap;

class Solution {

    public int findLHS(int[] nums) {
        Map<Integer, Integer> map = new TreeMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int result = 0;
        for (Integer key : map.keySet()) {
            if (key < Integer.MAX_VALUE && map.containsKey(key + 1)) {
                result = Math.max(result, map.get(key) + map.get(key + 1));
            }
        }
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-2, -1, 1, 3, 2, 2, 5, 2, 3, 7};
        int result = solution.findLHS(nums);
        System.out.println(result);
    }

}
