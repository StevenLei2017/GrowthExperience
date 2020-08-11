import java.util.Arrays;

public class Test {

    public static void main(String[] args) {
        int[] nums = new int[]{7, 6, 5, 2, 4, 5, 3, 9, 1, 8, 0};
        quickSort(nums, 0, nums.length - 1);
        System.out.println(Arrays.toString(nums));
    }

    private static void quickSort(int[] nums, int left, int right) {
        if(left >= right){
            return;
        }
        int l = left, r = right;
        int pivot = nums[l];
        while(l < r){
            while(l < r && nums[r] >= pivot){
                r -= 1;
            }
            if(l < r){
                nums[l] = nums[r];
                l += 1;
            }
            while(l < r && nums[l] < pivot){
                l += 1;
            }
            if(l < r){
                nums[r] = nums[l];
                r -= 1;
            }
        }
        nums[l] = pivot;
        System.out.println(Arrays.toString(nums));
        quickSort(nums, left, l - 1);
        quickSort(nums, l + 1, right);
    }

}
