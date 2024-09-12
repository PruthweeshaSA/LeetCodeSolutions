# class SmallestInfiniteSet:
# 
#     def __init__(self):
#         self.includeList = list(range(1,1001))
#         self.includeSet = set(self.includeList)
#         return
# 
#     def popSmallest(self) -> int:
#         op = self.includeList.pop(0) if len(self.includeSet) > 0 else 1000
#         self.includeSet.remove(op)
#         return op
# 
#     def addBack(self, num: int) -> None:
#         if num not in self.includeSet:
#             self.includeSet.add(num)
#             self.includeList = sorted(self.includeList+[num])
#         return
#         


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


class SmallestInfiniteSet:

    def __init__(self):
        self.includeList = list(range(1,1001))
        self.includeSet = set(self.includeList)
        return

    def popSmallest(self) -> int:
        op = self.includeList.pop(0)
        self.includeSet.remove(op)
        return op

    def addBack(self, num: int) -> None:
        if num in self.includeSet:
            return
        self.includeSet.add(num)
        start = 0
        end = len(self.includeList)-1
        mid = (start+end)//2

        if num < self.includeList[0]:
            self.includeList.insert(0,num)
            return

        if num > self.includeList[-1]:
            self.includeList.append(num)
            return

        while(start <= end):
            if self.includeList[mid] > num:
                if self.includeList[mid-1] < num:
                    self.includeList.insert(mid,num)
                    return
                end = mid - 1
            else:
                start = mid + 1
            mid = (start+end)//2
        return
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)