# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(head1,head2):
            res=ListNode()
            l3=res
            while head1 and head2:
                if head1.val<head2.val:
                    l3.next=ListNode(head1.val)
                    l3=l3.next
                    head1=head1.next
                else:
                    l3.next=ListNode(head2.val)    
                    l3=l3.next
                    head2=head2.next
            if head1:
                l3.next=head1
            if head2:
                l3.next=head2
            return res.next

        res=None
        for i in lists:
            res=merge(res,i)
        return res        