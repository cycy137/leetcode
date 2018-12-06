
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # i=0
        # tmp=[]
        # while head!=None:
        #     i+=1
        #     tmp.append(head.val)
        #     head=head.next
        # print (tmp[i//2:])

        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        print( head.val)
a=ListNode([1,2,3,4,5,6,7])
b=Solution.middleNode([],a)
