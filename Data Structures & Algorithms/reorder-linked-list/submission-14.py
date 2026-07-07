# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if  not head or not head.next:
            return None
        slow=fast=head
        prev1=None
        while(fast and fast.next):
            fast=fast.next.next
            prev1=slow
            slow=slow.next
        prev1.next=None

        curr, prev2= slow, None

        while(curr):
            nxt=curr.next
            curr.next=prev2
            prev2=curr
            curr=nxt

        tail=ListNode()
        list1=head
        list2=prev2
        while list1 and list2:
            nxt1=list1.next
            nxt2=list2.next
            tail.next=list1
            list1.next=list2
            tail=list2
            list1=nxt1
            list2=nxt2

        if list2:
            tail.next=list2
        return None    


        



            








            


        