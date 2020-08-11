class Solution {

    public String licenseKeyFormatting(String S, int K) {
        S = S.replace("-", "").toUpperCase();
        if (S == null || S.length() == 0) {
            return S;
        }
        StringBuilder stringBuilder = new StringBuilder();
        int remainder = S.length() % K;
        int index = remainder == 0 ? K : remainder;
        stringBuilder.append(S.substring(0, index));
        if (index != S.length()) {
            stringBuilder.append('-');
        }
        while (index < S.length()) {
            stringBuilder.append(S.substring(index, index + K));
            if (index + K != S.length()) {
                stringBuilder.append('-');
            }
            index += K;
        }
        return stringBuilder.toString();
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String S = "5F3Z-2e-9-w";
        String result = solution.licenseKeyFormatting(S, 4);
        System.out.println(result);
        S = "Abcd";
        result = solution.licenseKeyFormatting(S, 4);
        System.out.println(result);
        S = "---";
        result = solution.licenseKeyFormatting(S, 4);
        System.out.println(result);
    }

}
