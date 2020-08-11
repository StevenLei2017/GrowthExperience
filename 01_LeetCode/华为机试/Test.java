import java.util.HashMap;
import java.util.Map;

class Solution {

    Map<String, Integer> map = new HashMap<>();

    public Solution() {
        this.map.put("I", 1);
        this.map.put("II", 2);
        this.map.put("III", 3);
        this.map.put("IV", 4);
        this.map.put("V", 5);
        this.map.put("X", 10);
        this.map.put("XX", 20);
        this.map.put("XXX", 30);
        this.map.put("XL", 40);
        this.map.put("L", 50);
        this.map.put("C", 100);
        this.map.put("CC", 200);
        this.map.put("CCC", 300);
        this.map.put("CD", 400);
        this.map.put("D", 500);
        this.map.put("M", 1000);
        this.map.put("MM", 2000);
        this.map.put("MMM", 3000);
        this.map.put("CM", 900);
        this.map.put("XC", 90);
        this.map.put("IX", 9);
    }

    public int transform(String s) throws Exception {
        int index = 0;
        int result = 0;
        while (index < s.length()) {
            if (index + 3 <= s.length() && this.map.containsKey(s.substring(index, index + 3))) {
                result += this.map.get(s.substring(index, index + 3));
                index += 3;
            } else if (index + 2 <= s.length() && this.map.containsKey(s.substring(index, index + 2))) {
                result += this.map.get(s.substring(index, index + 2));
                index += 2;
            } else if (index + 1 <= s.length() && this.map.containsKey(s.substring(index, index + 1))) {
                result += this.map.get(s.substring(index, index + 1));
                index += 1;
            } else {
                throw new Exception("invalid input!");
            }

        }
        return result;
    }
}


public class Test {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        String testCase = "MCMACIV";
        int result = solution.transform(testCase);
        System.out.println(result);
        testCase = "LVIII";
        result = solution.transform(testCase);
        System.out.println(result);
        testCase = "IX";
        result = solution.transform(testCase);
        System.out.println(result);
        testCase = "IV";
        result = solution.transform(testCase);
        System.out.println(result);
        testCase = "III";
        result = solution.transform(testCase);
        System.out.println(result);
    }
}
