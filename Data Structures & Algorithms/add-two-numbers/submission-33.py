# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode()
        curr=dummy
        curr1=l1
        curr2=l2
        while(carry or curr1 or curr2):
            val1= curr1.val if curr1 else 0
            val2= curr2.val if curr2 else 0
            value=carry+val1+val2
            carry, val= divmod(value,10)
            curr.next=ListNode(val)
            curr=curr.next
            curr2=curr2.next if curr2 else None
            curr1=curr1.next if curr1 else None
        
        return dummy.next   




        