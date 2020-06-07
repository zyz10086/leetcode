# binary search tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class bst(object):
    root_node = None

    def __init__(self,root:TreeNode):
        root_node = TreeNode(root)

    def insert(self,node:TreeNode):
        

        pass
    def remove(self,val):
        pass
    def search(self,val):
        return self.searchByRecursive(self.root_node,val)

    #递归
    def searchByRecursive(self,node:TreeNode,val):
        if(not node):
            return
        if(node.val == val):
            return node
        if( node.left ):
            left_node = self.searchByRecursive(node,val)
            if(not left_node):
                return left_node
            

        pass
