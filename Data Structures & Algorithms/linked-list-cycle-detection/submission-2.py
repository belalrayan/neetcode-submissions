# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1, ptr2= head, head
        while ptr2:
            ptr2=ptr2.next
            if ptr2==None:
                return False
            else:
                ptr2=ptr2.next
            ptr1=ptr1.next
            if ptr1==ptr2:
                return True    

        return False            
        