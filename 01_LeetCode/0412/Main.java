import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= n; i += 1) {
            if (i % 3 == 0 && i % 5 == 0) {
                result.add("FizzBuzz");
            } else if (i % 3 == 0) {
                result.add("Fizz");
            } else if (i % 5 == 0) {
                result.add("Buzz");
            } else {
                result.add(String.valueOf(i));
            }
        }
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> result = solution.fizzBuzz(15);
        System.out.println(result);
    }

}
