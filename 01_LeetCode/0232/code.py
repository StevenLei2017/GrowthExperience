class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.number_list = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.number_list.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        pop_number = self.number_list.pop(0)
        return pop_number

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        peek_number = self.number_list[0]
        return peek_number
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """      
        return len(self.number_list) == 0    
       
       
if __name__ == '__main__':
    """ 主函数"""
    my_queue = MyQueue()
    my_queue.push(1)
    my_queue.push(2)
    print(my_queue.peek())
    print(my_queue.pop())
    print(my_queue.empty())
    