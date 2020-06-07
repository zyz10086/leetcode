# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.digui([99999,99999],root)
    def digui(self,limits,node):
        if(not node):
            return None
        cur_val = node.val
        down =abs(limits[0]-cur_val)
        up = abs(limits[1]-cur_val)
        min_val = down if down<up else up
        if(node.left):
            # 作为右节点 是上限
            left_val = self.digui([limits[0],node.val],node.left)
            if(left_val and left_val<min_val):
                min_val = left_val
        if(node.right):
            #作为左节点 是下限
            limits[0] = node.val
            right_val = self.digui([node.val,limits[1]],node.right)
            if(right_val and right_val<min_val):
                min_val = right_val
        return min_val

# [3220,1390,null,7,1855,null,null,null,2915]

root = TreeNode(1)
n1 = TreeNode(3)
n2 = TreeNode(2)

root.right = n1
n1.left = n2

s = Solution()
print(s.getMinimumDifference(root))