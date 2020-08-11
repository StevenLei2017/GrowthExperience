import java.util.Stack;

class Solution {

    public boolean find132pattern(int[] nums) {
        int middle = Integer.MIN_VALUE;
        Stack<Integer> stack = new Stack<>();
        for (int i = nums.length - 1; i >= 0; i -= 1) {
            if (nums[i] < middle) {
                return true;
            } else {
                while (!stack.isEmpty() && nums[i] > stack.peek()) {
                    middle = stack.pop();
                }
                stack.push(nums[i]);
            }
        }
        return false;
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 2, 3, 4};
        boolean result = solution.find132pattern(nums);
        System.out.println(result);
        nums = new int[]{3, 1, 4, 2};
        result = solution.find132pattern(nums);
        System.out.println(result);
    }

}
