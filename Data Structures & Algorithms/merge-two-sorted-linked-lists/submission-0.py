# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        if not list1 and not list2:
            return
        
        head1 = list1
        head2 = list2

        prev = ListNode(float('inf'))
        ret = prev
    
        while head1 and head2:
            val1 = head1.val
            val2 = head2.val

            newHead = None
            if val1 < val2:
                newHead = ListNode(val1)
                head1 = head1.next
            else:
                newHead = ListNode(val2)
                head2 = head2.next

            prev.next = newHead
            prev = prev.next

        if head1 and not head2:
            prev.next = head1
        
        if not head1 and head2:
            prev.next = head2
            
        
        return ret.next
