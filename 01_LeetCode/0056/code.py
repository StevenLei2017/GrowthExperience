class Solution(object):
    def merge(self, interval_list):
        if len(interval_list) == 0:
            return []
        interval_list.sort(key=lambda x: x[0])
        result_list = [interval_list[0]]
        for interval in interval_list[1:]:
            if interval[0] <= result_list[-1][-1]:
                result_list[-1][-1] = max(result_list[-1][-1], interval[-1])
            else:
                result_list.append(interval)
        return result_list        
              

if __name__ == '__main__':
    solution = Solution()
    interval_list = [[1,3], [2,6], [8,10], [15,18]]
    result_list = solution.merge(interval_list)
    print(result_list)