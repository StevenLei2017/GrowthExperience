class Solution:
    def strStr(self, haystack, needle):
        try:
            result = haystack.index(needle)
            return result
        except Exception:
            return -1
        

if __name__ == '__main__':
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    result = solution.strStr(haystack, needle)
    print(result)