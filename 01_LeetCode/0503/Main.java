import java.util.Arrays;
import java.util.Stack;

class Solution {

    public int[] nextGreaterElements(int[] nums) {
        if (nums == null || nums.length == 0) {
            return nums;
        }
        int length = nums.length;
        int[] result = new int[length];
        Arrays.fill(result, -1);
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < length * 2; i += 1) {
            int num = nums[i % length];
            while (!stack.isEmpty() && nums[stack.peek()] < num) {
                result[stack.pop()] = num;
            }
            if (i < length) {
                stack.push(i);
            }
        }
        return result;
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] testCase = {1, 2, 1};
        int[] result = solution.nextGreaterElements(testCase);
        System.out.println(Arrays.toString(result));
    }

}
