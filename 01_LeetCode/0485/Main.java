class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0, count = 0;
        for (int num : nums) {
            if (num == 1) {
                count += 1;
                result = Math.max(result, count);
            } else {
                count = 0;
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = new int[]{1, 1, 0, 1, 1, 1};
        int result = solution.findMaxConsecutiveOnes(nums);
        System.out.println(result);
    }
}
