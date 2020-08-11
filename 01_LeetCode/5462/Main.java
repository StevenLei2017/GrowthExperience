import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {

    public int getLengthOfOptimalCompression(String s, int k) {
        if (s == null || s.length() == 0 || s.length() == k) {
            return 0;
        }
        int i = 0;
        Map<Integer, Integer> map = new HashMap<>();
        while (i < s.length()) {
            int count = 1;
            while (i + 1 < s.length() && s.charAt(i) == s.charAt(i + 1)) {
                count += 1;
                i += 1;
            }
            map.put(count, map.getOrDefault(count, 0) + 1);
            i += 1;
        }
        int value = map.getOrDefault(1, 0) + map.getOrDefault(2, 0);
        if (k <= value) {
            int result = value - k;
            if (map.containsKey(1)) {
                map.remove(1);
            }
            if (map.containsKey(2)) {
                map.remove(2);
            }
            for (Integer key : map.keySet()) {
                int count = map.get(key);
                result = count * (1 + String.valueOf(key).length());
            }
            return result;
        } else {
            int result = 0;
            k -= value;
            PriorityQueue<Integer> priorityQueue = new PriorityQueue<Integer>();
            for (Integer key : map.keySet()) {
                for (int j = 0; j < map.get(key); j += 1) {
                    priorityQueue.offer(key);
                }
            }
            while (k > 0) {
                Integer count = priorityQueue.poll();
                System.out.println(k + " " + count);
                if (k >= count) {
                    k -= count;
                } else {
                    k = 0;
                    count -= k;
                    if (count < 3) {
                        result += count;
                    } else {
                        result += 1 + String.valueOf(count).length();
                    }
                }
            }
            while (!priorityQueue.isEmpty()) {
                Integer count = priorityQueue.poll();
                result += 1 + String.valueOf(count).length();
            }
            return result;
        }
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "aaabcccd";
        int result = solution.getLengthOfOptimalCompression(s, 2);
        System.out.println(result);
    }

}
