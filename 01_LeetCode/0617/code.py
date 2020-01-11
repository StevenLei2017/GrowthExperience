class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution(object):
    def mergeTrees(self, root_1, root_2):
        if not root_1 and not root_2:
            return None
        elif not root_1:
            return root_2
        elif not root_2:
            return root_1
        root_3 = TreeNode(root_1.val + root_2.val)
        root_3.left = self.mergeTrees(root_1.left, root_2.left)
        root_3.right = self.mergeTrees(root_1.right, root_2.right)
        return root_3

 
if __name__ == '__main__':
    solution = Solution()
    root_1 = TreeNode(1)
    root_2 = TreeNode(2)
    root_1.left = TreeNode(3)
    root_2.right = TreeNode(4)
    root_3 = solution.mergeTrees(root_1, root_2)
    print(root_3.val, root_3.left.val, root_3.right.val)
    