import java.util.HashSet;
import java.util.PriorityQueue;

class Solution {
    public int thirdMax(int[] nums) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        HashSet<Integer> hashSet = new HashSet<>();
        for (int num : nums) {
            if (hashSet.add(num)) {
                priorityQueue.offer(num);
                if (priorityQueue.size() > 3) {
                    priorityQueue.poll();
                }
            }
        }
        if (priorityQueue.size() == 2) {
            priorityQueue.poll();
        }
        return priorityQueue.peek();
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {3, 2, 1};
        int result = solution.thirdMax(nums);
        System.out.println(result);
        nums = new int[]{1, 2};
        result = solution.thirdMax(nums);
        System.out.println(result);
        nums = new int[]{2, 2, 3, 1};
        result = solution.thirdMax(nums);
        System.out.println(result);
    }

}
