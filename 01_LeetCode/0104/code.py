class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return 1 + max(left_depth, right_depth)
        

if __name__ == '__main__':
    solution = Solution()
    treeNode = TreeNode(1)
    treeNode.left = TreeNode(2)
    print(solution.maxDepth(treeNode))
    treeNode_1 = TreeNode(11)
    print(solution.maxDepth(treeNode_1))
    