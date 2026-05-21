# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        a=head
        l=0
        while a:
            l+=1
            a=a.next
        print(l)
        a=head
        l=l-n
        print(l)
        if l==0:
            return head.next
        for i in range(1,l+1):
            if(i==l):
                print(l,a.val)
                a.next=a.next.next
                break
            a=a.next
        return head
        