class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
               :type t1: TreeNode
               :type t2: TreeNode
               :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        else:
            if (not t1) and t2:
                t1=TreeNode(t2.val)
                t1.right = self.mergeTrees(t1.right , t2.right)
                t1.left = self.mergeTrees(t1.left , t2.left)
            elif t1 and t2:
                t1.val+=t2.val
                t1.right = self.mergeTrees(t1.right , t2.right)
                t1.left = self.mergeTrees(t1.left , t2.left)

            return t1
