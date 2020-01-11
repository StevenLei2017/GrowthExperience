class Solution:
    def fourSum(self, number_list, target):
        def findNsum(number_list, target, N, path, result_list):
            length = len(number_list)
            if length < N or N < 2 or target < number_list[0]*N or target > number_list[-1]*N:  # 及早终止
                return
            if N == 2:
                l, r = 0, length - 1
                while l < r:
                    s = number_list[l] + number_list[r]
                    if s == target:
                        result = path + [number_list[l], number_list[r]]
                        result_list.append(result)
                        l += 1
                        while l < r and number_list[l] == number_list[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(length-N+1):
                    if i == 0 or (i > 0 and number_list[i-1] != number_list[i]):
                        findNsum(number_list[i+1:], target-number_list[i], N-1, path+[number_list[i]], result_list)
        result_list = []
        number_list.sort()
        findNsum(number_list, target, 4, [], result_list)
        return result_list
    
                    
if __name__ == '__main__':
    solution = Solution()
    testCase = [1, 0, -1, 0, -2, 2]
    target = 0
    result_list = solution.fourSum(testCase, target)
    print(result_list)
    
    
        
    