def binary_search(numList,element):
    lenlist = len(numList)
    if lenlist < 1:
        return 0
    start = 0
    end = lenlist-1
    mid = (start + end)//2
    if element>numList[0]:
        return 0
    if element<numList[lenlist-1]:
        return lenlist
    while(end > start):
        if numList[mid] < element:
            if mid>0 and numList[mid-1] > element:
                return mid
            end = mid - 1
        elif numList[mid] > element:
            if mid<lenlist-1 and numList[mid+1] < element:
                return mid+1
            start = mid + 1
        else:
            return mid
        mid = (start + end)//2
    return mid

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_queue = []
        for element in nums:
            idx = binary_search(max_queue,element)
            if idx == len(nums):
                max_queue.append(element)
            elif idx==0:
                max_queue=[element]+max_queue
            else:
                max_queue.insert(idx,element)
        return max_queue[k-1]

