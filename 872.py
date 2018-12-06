class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def getNode(self,root):
            used=[root]
            tmp=[]
            while len(used)>0:
                node=used.pop()
                if node.left:
                    #node=node.left
                    used.append(node.left)
                if node.right:
                    used.append(node.right)
                if not node.right and not node.left:
                    tmp.append(node.val)
                return tmp

        return getNode(root1) == getNode(root2)



def getNode(root):
    used = [root]
    tmp = []
    while len(used) > 0:
        node = used.pop()
        print(node.left.left.left)
        if node.left:
            # node=node.left
            used.append(node.left)
        if node.right:
            used.append(node.right)
        if not node.right and not node.left:
            tmp.insert(0, node.val)
            print(node.val)
            # res.insert(0, node.val)
        # print (tmp)
    return tmp
    # print (getNode(root1) , getNode(root2))


return getNode(root1) == getNode(root2)