class Solution(object):
    def insert(self, interval_list, new_interval):
        if len(new_interval) == 0:
            pass
        elif len(interval_list) == 0 or new_interval[0] > interval_list[-1][0]:
            interval_list.append(new_interval)
        else:    
            N = len(interval_list)
            left, right = 0, N - 1
            value = new_interval[0]
            while left < right:
                middle = (left + right) // 2
                if interval_list[middle][0] < value:
                    left = middle + 1
                elif interval_list[middle][0] > value:
                    right = middle
                else:
                    break
            middle = (left + right) // 2
            interval_list.insert(middle, new_interval)    
        result_list = self.merge(interval_list)
        return result_list
        
    def merge(self, interval_list):
        if len(interval_list) == 0:
            return []
        result_list = [interval_list[0]]
        for interval in interval_list[1:]:
            last_result = result_list[-1]
            if interval[0] <= last_result[-1]:
                last_result[-1] = max(last_result[-1], interval[-1])
            else:
                result_list.append(interval)
        return result_list        
              

if __name__ == '__main__':
    solution = Solution()
    interval_list = [[1, 2]]
    new_interval = []
    result_list = solution.insert(interval_list, new_interval)
    print(result_list)