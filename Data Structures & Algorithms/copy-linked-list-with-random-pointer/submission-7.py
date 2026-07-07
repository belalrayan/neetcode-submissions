"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict={}
        curr=head
        while(curr):
            dict[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        while(curr):
            dict[curr].next=dict.get(curr.next,None)
            dict[curr].random=dict.get(curr.random,None)
            curr=curr.next
        return  dict.get(head,None)    
               

        