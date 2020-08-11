import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class NestedInteger {

    boolean isInt = true;

    int value;

    List<NestedInteger> list = new ArrayList<>();

    // Constructor initializes a single integer.
    public NestedInteger(int value) {
        this.isInt = true;
        this.value = value;
    }

    public NestedInteger(List<NestedInteger> list) {
        this.isInt = false;
        this.list = list;
    }

    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    public boolean isInteger() {
        return this.isInt;
    }

    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    public Integer getInteger() {
        return this.value;
    }

    // Set this NestedInteger to hold a single integer.
    public void setInteger(int value) {
        this.value = value;
    }

    // Set this NestedInteger to hold a nested list and adds a nested integer to it.
    public void add(NestedInteger ni) {
        if (this.isInt) {
            this.list.add(new NestedInteger(this.value));
        }
        this.list.add(ni);
        this.isInt = false;
    }

    // @return the nested list that this NestedInteger holds, if it holds a nested list
    // Return null if this NestedInteger holds a single integer
    public List<NestedInteger> getList() {
        return this.list;
    }

}

class Solution {

    int result;

    public int depthSum(List<NestedInteger> nestedList) {
        this.result = 0;
        if (nestedList == null) {
            return this.result;
        }
        this.helper(nestedList, 1);
        return this.result;
    }

    private void helper(List<NestedInteger> nestedList, int depth) {
        for (NestedInteger nestedInteger : nestedList) {
            if (nestedInteger.isInteger()) {
                this.result += nestedInteger.getInteger() * depth;
            } else {
                this.helper(nestedInteger.getList(), depth + 1);
            }
        }
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        NestedInteger nestedInteger1 = new NestedInteger(1);
        NestedInteger nestedInteger4 = new NestedInteger(4);
        NestedInteger nestedInteger6 = new NestedInteger(Arrays.asList(new NestedInteger(6)));
        nestedInteger4.add(nestedInteger6);
        nestedInteger1.add(nestedInteger4);
        int result = solution.depthSum(nestedInteger1.getList());
        System.out.println(result);
    }

}
