class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case: empty list or last node
        if not head or not head.next:
            return head


        new_head=self.reverseList(head.next)

        head.next.next=head

        head.next=None

        return new_head