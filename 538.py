class Solution(object):
    def convertBST(self, root):

        # if not root:
        #     return []
        # print(root.val)
        # print(root.right)
        # print(root.left)
        # if root.left and root.right:
        #
        #     root.left.val = root.val + root.left.val + root.right.val
        #     root.val = root.val + root.right.val
        #     return root
        # elif root.left:
        #     root.left.val = root.val + root.left.val
        #     return root
        # elif not root.left and not root.right:
        #     return root
        # else:
        #     return root
        def way(root,num):
            if not root:
                return 0
            right=way(root.right,num)
            left=way(root.left,num+root.val+right)
            val=root.val
            root.val=root.val+num+right
            return val+left+right
        way(root,0)
        return root
