# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d=[]
        a=head
        while a:
            if a in d:
                return True
            d.append(a)
            a=a.next
        return False