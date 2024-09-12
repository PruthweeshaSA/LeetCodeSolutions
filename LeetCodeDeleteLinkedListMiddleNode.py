# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        while node is not None:
            count += 1
            node=node.next
        if count < 2:
            return head.next
        count //= 2
        node = head
        for i in range(count-1):
            node = node.next
        node.next = node.next.next
        return head
        