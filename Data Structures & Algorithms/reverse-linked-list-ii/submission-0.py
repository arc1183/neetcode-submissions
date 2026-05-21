# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=1
        l1=head
        head2=ListNode()
        l2=head2
        while l!=left:
            n=ListNode(l1.val)
            l2.next=n
            l2=l2.next
            l1=l1.next
            l+=1
        print(head2,l1)
        mid=l2
        tail=None
        p=tail
        while l<right+1:
            n=ListNode(l1.val)
            n.next=p
            p=n
            l1=l1.next
            l+=1
        l2.next=p
        while l2.next:
            l2=l2.next
        if l1:
            l2.next=l1

        print(head2)
        return head2.next