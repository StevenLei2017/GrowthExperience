import java.util.Arrays;

class Solution{
    public int removeElement(int[] nums, int value){
        if(nums == null || nums.length == 0){
            return 0;
        }
        int oldIndex = 0, newIndex = 0;
        while (oldIndex < nums.length){
            if(nums[oldIndex] == value){
                oldIndex += 1;
            } else{
                nums[newIndex] = nums[oldIndex];
                oldIndex += 1;
                newIndex += 1;
            }
        }
        return newIndex;
    }
}


public class Main{
    public static void main(String[] args) {
        int[] nums = new int[]{0, 1, 2, 2, 3, 0, 4, 2};
        int value = 2;
        Solution solution = new Solution();
        int result = solution.removeElement(nums, value);
        System.out.println(result);
        System.out.println(Arrays.toString(nums));
    }
}