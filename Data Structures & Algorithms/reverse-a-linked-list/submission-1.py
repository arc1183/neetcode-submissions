# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=None
        a=head
        while a:
            node=ListNode(a.val)
            node.next=p
            p=node
            a=a.next
        return p
            

            
        