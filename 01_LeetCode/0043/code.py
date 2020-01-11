class Solution(object):
    def multiply(self, number1_string, number2_string):
        number1 = int(number1_string)
        number2 = int(number2_string)
        number3 = number1 * number2
        number3_string = str(number3)
        return number3_string
        

if __name__ == '__main__':
    solution = Solution()
    number1_string = '123'
    number2_string = '456'
    result = solution.multiply(number1_string, number2_string)
    print(result)
    