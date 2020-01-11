class Solution(object):
    def diameterOfBinaryTree(self, root_treeNode):
        self.result = 0
        def get_depth(treeNode):
            if not treeNode:
                return 0
            left_depth = get_depth(treeNode.left)
            right_depth = get_depth(treeNode.right)
            self.result = max(self.result, left_depth+right_depth)
            depth = 1 + max(left_depth, right_depth)
            return depth
        get_depth(root_treeNode)
        return self.result
        
        
        
if __name__ == '__main__':
    solution = Solution()   
        
    