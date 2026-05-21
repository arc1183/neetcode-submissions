# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        n=head
        carry=0
        while l1 and l2:
            a=(l1.val+l2.val+carry)
            carry= a//10
            a=a%10
            n.next=ListNode(a)
            n=n.next
            l1=l1.next
            l2=l2.next
        while l1:
            a=l1.val+carry
            carry=a//10
            a=a%10
            n.next=ListNode(a)
            n=n.next
            l1=l1.next
        while l2:
            a=l2.val+carry
            carry=a//10
            a=a%10
            n.next=ListNode(a)
            n=n.next
            l2=l2.next
        if carry:
            n.next=ListNode(carry)
        return head.next