# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(not root):
            return [[root.val]]
        res = []
        self.digui(1,root,res)
        return res
    def digui(self,level,node,res):
        if(node):
            if(len(res)>=level):
                res[level-1].append(node.val)
            else:
                res.insert(level-1,[node.val])
        if(not node.left and not node.right):
            return
        if( node.left ):
            self.digui(level+1,node.left,res)
        if ( node.right):
            self.digui(level+1,node.right,res)

root = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)
root.left = t1
root.right = t2
t2.left = t3
t2.right = t4
s = Solution()
print(s.levelOrder(root))