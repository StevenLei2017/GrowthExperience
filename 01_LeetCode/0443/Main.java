import java.util.Arrays;

class Solution {

    public int compress(char[] chars) {
        int i = 0, compressIndex = 0, result = 0;
        while (i < chars.length) {
            int count = 1;
            while (i + 1 < chars.length && chars[i] == chars[i + 1]) {
                i += 1;
                count += 1;
            }
            chars[compressIndex] = chars[i];
            compressIndex += 1;
            result += 1;
            if (count != 1) {
                char[] number = String.valueOf(count).toCharArray();
                for (int j = 0; j < number.length; j += 1) {
                    chars[compressIndex] = number[j];
                    compressIndex += 1;
                }
                result += number.length;
            }
            i += 1;
        }
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "aaabbaa";
        char[] input = s.toCharArray();
        System.out.println(Arrays.toString(input));
        int result = solution.compress(input);
        System.out.println(result);
        System.out.println(Arrays.toString(input));
    }

}
