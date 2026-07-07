# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        fast = slow= head
        prev1=None
        while(fast and fast.next):
            fast=fast.next.next
            prev1=slow
            slow=slow.next
        prev1.next=None

        curr, prev2=slow, None
        while(curr):
            nxt=curr.next
            curr.next=prev2
            prev2=curr
            curr=nxt

        list2=prev2
        list1=head
        dummy=ListNode()
        tail=dummy
        curr=None
        while list1 and list2:
            nxt1 = list1.next
            nxt2 = list2.next
            tail.next = list1
            list1.next = list2
            list1 = nxt1
            list2 = nxt2
            tail = tail.next.next if tail.next.next else tail.next
        
        return None


            








            


        