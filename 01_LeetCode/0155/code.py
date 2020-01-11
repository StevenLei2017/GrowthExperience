class MinStack(object):
    def __init__(self):
        """ 最小栈类的实例化对象后的初始化"""
        self.stack = []
        self.min_list = []
        
    def push(self, value):
        """ 入栈"""
        self.stack.append(value)
        if not self.min_list:
            self.min_list.append(value)
        else:
            min_value = min(self.min_list[-1], value)
            self.min_list.append(min_value)
        
    def pop(self):
        """ 出栈"""
        self.stack.pop()
        self.min_list.pop()
        
    def top(self):
        """ 获取栈顶端的值"""
        return self.stack[-1]
        
    def getMin(self):
        """ 获取栈里面的最小值"""
        return self.min_list[-1]
        

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())   # Returns -3.
    minStack.pop()
    print(minStack.top())     # Returns 0.
    print(minStack.getMin())  # Returns -2.
    