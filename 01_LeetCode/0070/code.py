class Solution(object):
    def __init__(self):
        self.record_dict = {}
    
    def climbStairs(self, number):
        if number < 4:
            return number
        if number in self.record_dict:
            return self.record_dict[number]
        else:        
            result = self.climbStairs(number-1) + self.climbStairs(number-2)
            self.record_dict[number] = result
            return result

 
if __name__ == '__main__':
    solution = Solution()