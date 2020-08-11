class Solution {

    public int minMoves(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return 0;
        }
        int sum = 0, min = Integer.MAX_VALUE;
        for (int num : nums) {
            sum += num;
            min = Math.min(min, num);
        }
        int result = sum - min * nums.length;
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.minMoves(new int[]{1, 2, 3});
        System.out.println(result);
    }

}
