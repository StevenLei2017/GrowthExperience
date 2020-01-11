class Solution(object):
    def plusOne(self, digit_list):
        digitChar_list = [str(k) for k in digit_list]
        number = int(''.join(digitChar_list))
        number += 1
        result_list = [int(k) for k in str(number)]
        return result_list
        

if __name__ == '__main__':
    solution = Solution()
    digit_list = [4,3,2,1]
    result_list = solution.plusOne(digit_list)
    print(result_list)