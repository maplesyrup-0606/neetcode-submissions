# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return

        root = head
        prev = None
    
        while root:
            next_ = root.next
            root.next = prev

            if next_:
                prev = root
                root = next_
            else:
                return root