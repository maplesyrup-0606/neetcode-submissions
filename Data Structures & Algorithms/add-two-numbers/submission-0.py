# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2: return l2
        if l1 and not l2: return l1
        if not l1 and not l2: return
    
        carry = 0
        newHead = ListNode(-1)
        root = newHead
        while l1 and l2:
            newVal = l1.val + l2.val + carry
            carry = newVal // 10
            newVal = newVal % 10
        
            newNext = ListNode(newVal)
            newHead.next = newNext
            newHead = newHead.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                newVal = l1.val + carry
                carry = newVal // 10
                newVal = newVal % 10
            
                newNext = ListNode(newVal)
                newHead.next = newNext
                newHead = newHead.next
                l1 = l1.next
        elif l2:
            while l2:
                newVal = l2.val + carry
                carry = newVal // 10
                newVal = newVal % 10
            
                newNext = ListNode(newVal)
                newHead.next = newNext
                newHead = newHead.next
                l2 = l2.next
        
        if carry:
            newNext = ListNode(carry)
            newHead.next = newNext
            newHead = newHead.next
        return root.next