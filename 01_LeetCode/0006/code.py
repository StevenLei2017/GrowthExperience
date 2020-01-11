class Solution(object):
    def convert(self, input_string, N_row):
        if N_row == 1:
            return input_string
        line_list = [''] * N_row
        n = N_row - 1
        for i, char in enumerate(input_string):
            j = i // n
            if j & 1:
                row_index = n - i % n
            else:
                row_index = i % n
            line_list[row_index] += char
        output_string = ''.join(line_list)    
        return output_string

                    
if __name__ == '__main__':
    solution = Solution()
    s = "PAYPALISHIRING"
    N_row = 3
    result = solution.convert(s, N_row)
    print(result)
    s = "PAYPALISHIRING"
    N_row = 4
    result = solution.convert(s, N_row)
    print(result)
    s = "ABC"
    N_row = 1
    result = solution.convert(s, N_row)
    print(result)
    s = "ABCD"
    N_row = 2
    result = solution.convert(s, N_row)
    print(result)