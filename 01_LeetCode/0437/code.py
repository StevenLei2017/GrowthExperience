class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def pathSum_0(self, root, target):
        self.count = 0
        def helper(root):
            if not root:
                return []
            sum_list = [root.val] + [root.val + k for k in helper(root.left) + helper(root.right)]
            self.count += sum_list.count(target)
            return sum_list
        helper(root)    
        return self.count
     
    def pathSum(self, root, target):
        self.count = 0
        record_dict = {0: 1}
        def dfs(treeNode, previous_sum):
            if not treeNode:
                return
            current_sum = previous_sum + treeNode.val
            # 当前节点的累加和减去目标和的差值在记录字典中
            diff_value = current_sum - target
            if diff_value in record_dict:
                self.count += record_dict[diff_value]       
            if current_sum in record_dict:
                record_dict[current_sum] += 1
            else:
                record_dict[current_sum] = 1
            dfs(treeNode.left, current_sum)
            dfs(treeNode.right, current_sum)
            record_dict[current_sum] -= 1
        dfs(root, 0)
        return self.count
            
    
def get_depth(treeNode):
    if not treeNode:
        return 0
    else:
        return 1 + max(get_depth(treeNode.left), get_depth(treeNode.right))


import math
def get_root_treeNode(number_list):
    if not number_list:
        return None
    treeNode_list = []
    for number in number_list:
        if number:
            treeNode = TreeNode(number)
        else:
            treeNode = None
        treeNode_list.append(treeNode)
    length = len(number_list)    
    for i in range(length//2):
        if treeNode_list[i]:
            if 2 * i + 1 < length:
                treeNode_list[i].left = treeNode_list[2 * i + 1]
            if 2 * i + 2 < length:
                treeNode_list[i].right = treeNode_list[2 * i + 2]
    return treeNode_list[0]            
    
       
if __name__ == '__main__':
    """ 主函数"""
    solution = Solution()
    number_list = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root_treeNone = get_root_treeNode(number_list)
    print(get_depth(root_treeNone))
    print(solution.pathSum(root_treeNone, 8))
    
    
    