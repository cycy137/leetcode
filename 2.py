# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry=0
        ret=l1
        last=ret
        while l1 or l2:
            if l1 and l2:
                l1.val+=l2.val+carry
            elif l1:
               l1.val+=carry
            elif l2:
                last.next=l2
                l1=last.next
                l1.val+=carry
                l2=None
            if l1.val>9:
                carry=1
                l1.val_=10
            else :
                carry=0
            last=l1
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            last.next=ListNode(0)
        return ret
