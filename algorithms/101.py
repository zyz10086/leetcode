#给定一个二叉树，检查它是否是镜像对称的。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(not root):
            return True
        tree_node = [root]
        index = 0
        max_index = 0
        if(root.left):
            max_index = 1
        if(root.right):
            max_index = 2
        while(index<max_index):
            index += 1
            parent_index = (index-1) >> 1
            left_node = (index % 2) ==1
            if(left_node):
                tree_node.append(tree_node[parent_index].left if tree_node[parent_index] else None )
            else:
                tree_node.append(tree_node[parent_index].right if tree_node[parent_index] else None)
            if(tree_node[index]):
                max_index = index*2+2
        node_len = len(tree_node)
        level = 2
        start_index = 1
        while(start_index<node_len-1):
            ary_len = 2**level - 1
            ary_len_half = (2**(level - 1)) >>1
            res = self.juage(tree_node[start_index:start_index+ary_len_half],tree_node[start_index+ary_len_half:ary_len])
            if not res:
                return res
            start_index = ary_len
            level +=1
        return True

    def juage(self,left_node,right_node):
        left_len,right_len = len(left_node),len(right_node)
        left,right = 0,right_len-1
        if(left_len!=right_len):
            for v in range(left_len):
                if(left_node[v]):
                    return False
            for v in range(right_len):
                if(right_node[v]):
                    return False
            return True
        while(left<left_len):
            if(left_node[left] and right_node[right]):
                if(left_node[left].val!=right_node[right].val):
                    return False
            else:
                if(left_node[left] or right_node[right] ):
                    return False
            left += 1
            right -= 1
        return True

s = Solution()
root = TreeNode(5)
n1 = TreeNode(4)
n2 = TreeNode(1)
n3 = TreeNode(4)
n4 = TreeNode(2)
n5 = TreeNode(2)
n6 = TreeNode(1)

root.left = n1

n1.right = n2
n2.left = n4

root.right = n6
n4.right = n3
n3.left = n5

root2 = TreeNode(1)
root2.right = TreeNode(2)

root3 = TreeNode(4)
root3.left = TreeNode(-57)
root3.right = TreeNode(-57)
root3.left.right = TreeNode(67)
root3.right.left = TreeNode(67)
root3.left.right.right = TreeNode(-97)
root3.right.left.left = TreeNode(-97)
print(s.isSymmetric(root3))