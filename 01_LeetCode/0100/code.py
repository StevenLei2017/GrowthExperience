class Solution:
    def isSameTree(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        elif not root_1 or not root_2:
            return False
        elif root_1.val == root_2.val and self.isSameTree(root_1.left, root_2.left) and self.isSameTree(root_1.right, root_2.right):
            return True
        else:
            return False
        

if __name__ == '__main__':
    solution = Solution()