class Solution(object):
    def intToRoman(self, number):
        value2roman_dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'}
        result = ''
        for key in value2roman_dict.keys():
            while number >= key:
                quotient = number // key
                result += value2roman_dict[key] * quotient
                number -= key * quotient
        return result
        
                    
if __name__ == '__main__':
    solution = Solution()
    number = 1994
    result = solution.intToRoman(number)
    print(result)
    
        
    