# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0
        curr1, curr2= l1, l2
        i1=i2=1
        while(curr1):
            num1+=(curr1.val* i1)
            i1*=10
            curr1=curr1.next
        while(curr2):
            num2+=(curr2.val* i2)
            i2*=10
            curr2=curr2.next    

        sum=num1+num2
        if(not sum):return ListNode(0)
        curr=None
        i=1
        sum2=sum
        while(sum2>0):
            i*=10
            sum2//=10
        
        if  i>1:
            i=i//10
        while i>0:
            num,remainder=divmod(sum,i)
            curr=ListNode(num,curr)
            sum=remainder
            i= i//10
        return curr





        