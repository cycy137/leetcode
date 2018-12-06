class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first=None
        while head:
            head.next,first,head=first,head,head.next
            return first
a=[1,2,3,4,5]
b=ListNode(a)
c=Solution.reverseList([],b)
print(b)
print(c)