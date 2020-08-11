import java.util.*;

class Solution {

    public int leastBricks(List<List<Integer>> wall) {
        if (wall == null || wall.size() == 0 || wall.get(0).size() == 0) {
            return -1;
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (List<Integer> row : wall) {
            int currentWidth = 0;
            for (int i = 0; i < row.size() - 1; i += 1) {
                int width = row.get(i);
                currentWidth += width;
                int currentCount = map.getOrDefault(currentWidth, 0) + 1;
                map.put(currentWidth, currentCount);
            }
        }
        int height = wall.size();
        int maxCount = 0;
        for (int value : map.values()) {
            maxCount = Math.max(maxCount, value);
        }
        return height - maxCount;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<List<Integer>> inputs = new ArrayList<>();
        inputs.add(Arrays.asList(1, 2, 2, 1));
        inputs.add(Arrays.asList(3, 1, 2));
        inputs.add(Arrays.asList(1, 3, 2));
        inputs.add(Arrays.asList(2, 4));
        inputs.add(Arrays.asList(3, 1, 2));
        inputs.add(Arrays.asList(1, 3, 1, 1));
        int result = solution.leastBricks(inputs);
        System.out.println(result);
    }

}
