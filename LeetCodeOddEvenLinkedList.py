# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        evenStack = head
        evenStackEnd = head
        oddStack = head.next
        oddStackEnd = oddStack
        temp = oddStackEnd.next
        odd = False
        while temp is not None:
            if odd:
                odd = False
                oddStackEnd.next = temp
                oddStackEnd = temp
            else:
                odd = True
                evenStackEnd.next = temp
                evenStackEnd = temp
            temp=temp.next
        oddStackEnd.next=None
        evenStackEnd.next = oddStack
        return evenStack
        