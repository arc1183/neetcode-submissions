# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def check(head):
            i=1
            while head and i<=k:
                head=head.next
                i+=1
            return True if i>k else False
        def reverse(head):
            rev=head
            p=None
            i=1
            while head and i<=k :
                q=head.next
                head.next=p
                p=head
                head=q
                i+=1
            h=head
            return p,rev,h
        h=head
        result=ListNode()
        prev=result
        while h and check(h):
            p,rev,h=reverse(h)
            prev.next=p
            prev=rev
        if not check(h):
            prev.next=h
        return result.next