import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {

    List<Integer> list = Arrays.asList(new Integer[]{2, 3, 4, 5, 7});

    Map<Integer, Integer> map = new HashMap<>();

    public Solution() {
        this.map.put(0, 0);
        this.map.put(1, 1);
        this.map.put(6, 9);
        this.map.put(8, 8);
        this.map.put(9, 6);
    }

    public boolean confusingNumber(int N) {
        if (N == 0) {
            return false;
        }
        StringBuilder stringBuilder = new StringBuilder();
        int sourceN = N;
        while (N > 0) {
            int remainder = N % 10;
            if (this.list.contains(remainder)) {
                return false;
            }
            stringBuilder.append(this.map.get((remainder)));
            N /= 10;
        }
        int reversedN = Integer.valueOf(stringBuilder.toString());
        return sourceN != reversedN;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int testCase = 6;
        boolean result = solution.confusingNumber(testCase);
        System.out.println(result);
        testCase = 89;
        result = solution.confusingNumber(testCase);
        System.out.println(result);
        testCase = 11;
        result = solution.confusingNumber(testCase);
        System.out.println(result);
        testCase = 52;
        result = solution.confusingNumber(testCase);
        System.out.println(result);
    }

}
