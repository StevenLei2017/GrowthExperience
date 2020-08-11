import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> readBinaryWatch(int num) {
        List<String> result = new ArrayList<>();
        for(int hour = 0; hour < 12; hour += 1){
            for(int minute = 0; minute < 60; minute += 1){
                if(Integer.bitCount(hour) + Integer.bitCount(minute) == num){
                    result.add(String.format("%d:%02d", hour, minute));
                }
            }
        }
        return result;
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> result = solution.readBinaryWatch(1);
        System.out.println(result);
    }

}
