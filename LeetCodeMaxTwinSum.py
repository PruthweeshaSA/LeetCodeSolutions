# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        linearTraversal = []
        node=head
        while(node is not None):
            linearTraversal.append(node.val)
            node=node.next

        maximum = 0
        length = len(linearTraversal)
        for i in range(int(length/2)):
            if linearTraversal[i] + linearTraversal[length-1-i] > maximum:
                maximum = linearTraversal[i] + linearTraversal[length-1-i] 
        
        return maximum