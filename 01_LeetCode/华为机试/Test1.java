import java.util.*;

class Solution1 {

    public int solve(List<List<Integer>> inputs) {
        if (inputs == null || inputs.size() == 0 || inputs.get(0).size() == 0) {
            return -1;
        }
        Map<Integer, Integer> map = new HashMap<>();
        int maxWidth = 0;
        maxWidth = inputs.get(0).stream().mapToInt(Integer::intValue).sum();
        for (List<Integer> row : inputs) {
            int allWidth = 0;
            for (Integer boxWidth : row) {
                allWidth += boxWidth;
                map.put(allWidth, map.getOrDefault(allWidth, 0) + 1);
            }
        }
        int maxRowLineThrough = 0;
        for (int i = 1; i < maxWidth; i += 1) {
            if (map.containsKey(i) && map.get(i) > maxRowLineThrough) {
                maxRowLineThrough = map.get(i);
            }
        }
        int height = inputs.size();
        return height - maxRowLineThrough;
    }

}

public class Test1 {

    public static void main(String[] args) {
        Solution1 solution = new Solution1();
        List<List<Integer>> list = new ArrayList<>();
        list.add(Arrays.asList(new Integer[]{1, 2, 2, 1}));
        list.add(Arrays.asList(new Integer[]{3, 1, 2}));
        list.add(Arrays.asList(new Integer[]{1, 3, 2}));
        list.add(Arrays.asList(new Integer[]{2, 4}));
        list.add(Arrays.asList(new Integer[]{3, 1, 2}));
        list.add(Arrays.asList(new Integer[]{1, 3, 1, 1}));
        int result = solution.solve(list);
        System.out.println(result);
    }

}

