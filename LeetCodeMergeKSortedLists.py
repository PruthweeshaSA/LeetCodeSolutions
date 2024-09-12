# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numLists = len(lists)
        if numLists == 0:
            return None
        minElement = 10*10
        resultant = []
        while True:
            allEmpty = True
            for listHeadIndex in range(len(lists)):
                listHead = lists[listHeadIndex]
                if listHead is None:
                    continue
                allEmpty = False
                if listHead.val < minElement:
                    minElement = listHead.val
                    minNodeIndex = listHeadIndex
            if allEmpty:
                break
            resultant.append(minElement)
            lists[minNodeIndex] = lists[minNodeIndex].next
            minElement = lists[minNodeIndex].val if lists[minNodeIndex] is not None else 10*10
        if len(resultant) == 0:
            return None
        node = ListNode(resultant[0])
        head = node 
        for element in resultant[1:]:
            node.next = ListNode(element)
            node = node.next
        return head