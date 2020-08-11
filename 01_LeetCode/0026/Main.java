import java.util.Arrays;

class Solution{
    public int removeDuplicates(int[] nums){
        if(nums == null || nums.length == 0){
            return 0;
        }
        int quantity = 1,  value = nums[0];
        int oldIndex = 1, newIndex = 1;
        while(oldIndex < nums.length){
            if(nums[oldIndex] == nums[oldIndex - 1]){
                oldIndex += 1;
            } else{
                nums[newIndex] = nums[oldIndex];
                oldIndex += 1;
                newIndex += 1;
                quantity += 1;
            }
        }
        return quantity;
    }
}

public class Main{
    public static void main(String[] args) {
        int[] nums = new int[]{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        Solution solution = new Solution();
        int quantity = solution.removeDuplicates(nums);
        System.out.println(quantity);
        System.out.println(Arrays.toString(nums));
    }
}