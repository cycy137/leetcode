class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i=2
        first=mid=ListNode(0)
        while l1 and l2:
            if i%2==0:
                print("sdfsf")
                mid.next=l1.next
                print(l1.next.val)
                mid=mid.next
                print(mid)
                l1=l1.next
            else:
                mid.next=l2.next
                mid=mid.next
                l2=l2.next
            i+=1
            print(mid)
        return first.next

l1=ListNode([1,2,4])
l2=ListNode([1,3,4])
a=Solution.mergeTwoLists([],l1,l2)
print(a)

