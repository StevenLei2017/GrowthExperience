class Solution(object):
    def longestValidParentheses(self, s):
        stack = [0]
        longest = 0
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                if len(stack) > 1:  
                    value = stack.pop()
                    stack[-1] += value + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest
            

if __name__ == '__main__':
    solution = Solution()
    s = "(()(((()"
    result = solution.longestValidParentheses(s)
    print(result)
    s = ")()())"
    result = solution.longestValidParentheses(s)
    print(result)
    s = "()(()"
    result = solution.longestValidParentheses(s)
    print(result)
    