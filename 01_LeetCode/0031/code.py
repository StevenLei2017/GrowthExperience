class Solution(object):
    def nextPermutation(self, number_list):
        N = len(number_list)
        i = N - 1
        while i  > 0 and number_list[i-1] >= number_list[i]:
            i -= 1
        if i == 0:
            number_list.reverse()
            return 
        k = i - 1
        j = N - 1
        while number_list[j] <= number_list[k]:
            j -= 1
        number_list[k], number_list[j] = number_list[j], number_list[k]
        left, right = k + 1, N -1
        while left < right:
            number_list[left], number_list[right] = number_list[right], number_list[left]
            left += 1
            right -= 1
        
            

if __name__ == '__main__':
    solution = Solution()
    number_list = [1, 2, 3]
    solution.nextPermutation(number_list)
    print(number_list)
    number_list = [3, 2, 1]
    solution.nextPermutation(number_list)
    print(number_list)
    number_list = [1, 1, 5]
    solution.nextPermutation(number_list)
    print(number_list)
    
    