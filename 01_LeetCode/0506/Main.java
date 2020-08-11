import java.util.Arrays;

class Solution {

    public String[] findRelativeRanks(int[] nums) {
        if (nums == null || nums.length == 0) {
            return new String[0];
        }
        String[] result = new String[nums.length];
        int max = 0;
        for (int num : nums) {
            max = Math.max(max, num);
        }
        int[] bucket = new int[max + 1];
        Arrays.fill(bucket, -1);
        for (int i = 0; i < nums.length; i += 1) {
            int num = nums[i];
            bucket[num] = i;
        }
        int rank = 1;
        for (int i = bucket.length - 1; i >= 0; i -= 1) {
            int index = bucket[i];
            if (index >= 0) {
                result[index] = this.getRankString(rank);
                rank += 1;
            }
        }
        return result;
    }

    private String getRankString(int rank) {
        if (rank > 3) {
            return String.valueOf(rank);
        } else if (rank == 1) {
            return "Gold Medal";
        } else if (rank == 2) {
            return "Silver Medal";
        } else if (rank == 3) {
            return "Bronze Medal";
        }
        return String.valueOf(rank);
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] testCase = {5, 4, 3, 2, 1};
        String[] result = solution.findRelativeRanks(testCase);
        System.out.println(Arrays.toString(result));
    }

}
