# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return
    
        """
        1. Get length and find that position to remove : O(n), requires two traversals
        """

        length = 0
        root = head
        while root:
            length += 1
            root = root.next
        
        find = length - n
    
        check = head
        prev = None
        i = 0
        while check:
            if i == find:
                if not prev:
                    if length == 1:
                        return None
                    else:
                        return check.next
                prev.next = check.next
                return head
            prev = check
            check = check.next
            i += 1
        
        return head