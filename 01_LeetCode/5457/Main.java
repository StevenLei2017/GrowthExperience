class Solution {

    public int numOfSubarrays(int[] arr) {
        int oddCount = 0, evenCount = 0;
        if (arr == null || arr.length == 0) {
            return 0;
        }
        for (int number : arr) {
            if (number % 2 == 0) {
                evenCount += 1;
            } else {
                oddCount += 1;
            }
        }
        if (oddCount == 0) {
            return 0;
        }
        int allCount = oddCount + evenCount - 1;
        int result = 1;
        for (int i = 0; i < allCount; i += 1) {
            result = (result * 2) % 1000000007;
        }
        return result;
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr = {1, 3, 5};
        int result = solution.numOfSubarrays(arr);
        System.out.println(result);
        arr = new int[]{2, 4, 6};
        result = solution.numOfSubarrays(arr);
        System.out.println(result);
        arr = new int[]{1, 2, 3, 4, 5, 6, 7};
        result = solution.numOfSubarrays(arr);
        System.out.println(result);
        arr = new int[]{100, 100, 99, 99};
        result = solution.numOfSubarrays(arr);
        System.out.println(result);
        arr = new int[]{7};
        result = solution.numOfSubarrays(arr);
        System.out.println(result);
    }

}
