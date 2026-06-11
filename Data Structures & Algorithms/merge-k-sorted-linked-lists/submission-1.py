# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return
        def merge_two_sorted_lists(list1, list2):
            root = ListNode(-1)
            base = root
            while list1 and list2:
                if list1.val > list2.val:
                    root.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    root.next = ListNode(list1.val)
                    list1 = list1.next
                
                root = root.next

            if list1 and not list2:
                root.next = list1
            
            if list2 and not list1:
                root.next = list2
            
            return base.next

        def print_list(root):
            res = ""
            while root:
                res += str(root.val) + " "
                root = root.next        
            print(res)
        
        lists = deque(lists)

        while len(lists) > 1:
            one = lists.popleft()
            two = lists.popleft()
            newList = merge_two_sorted_lists(one, two)
            lists.append(newList)
        
        return lists[0]
