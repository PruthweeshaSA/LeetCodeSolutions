def make_minheap(list_int):
    result = []
    for i in range(len(list_int)):
        element = list_int[i]
        middle = int(len(result)/2)
        if (len(result)==0):
            result=[element]
        elif element <= result[middle]:
            if len(result) == 1:
                result += [element]
            elif len(result)%2 == 1:
                result.insert(middle+1,element)
            else:
                result.insert(middle,element)
        elif len(result)%2 == 0:
            # odd number of nodes in resultant heap:
            # insert to right branch
            inserted = False
            for j in range(middle,len(result)):
                if element <= result[j]:
                    result.insert(j,element)
                    inserted = True
                    break
            if not inserted:
                result.append(element)
        else:
            # even number of nodes in resultant heap:
            # insert to left branch
            inserted = False
            for j in range(middle,-1,-1):
                if element <= result[j]:
                    result.insert(j+1,element)
                    inserted = True
                    break
            if not inserted:
                result = [element] + result

    return result

def insert_to_minheap(minheap,element):
    if len(minheap) == 0:
        return [element]
    middle = int(len(minheap)/2)
    if element <= minheap[middle]:
        if len(minheap)%2 == 1:
            minheap.insert(middle+1,element)
        else:
            minheap.insert(middle,element)
    elif len(minheap)%2 == 0:
        # odd number of nodes in resultant heap:
        # insert to right branch
        inserted = False
        for j in range(middle+1,len(minheap)):
            if element <= minheap[j]:
                minheap.insert(j,element)
                inserted = True
                break
        if not inserted:
            minheap.append(element)
    else:
        # even number of nodes in resultant heap:
        # insert to left branch
        inserted = False
        for j in range(middle,-1,-1):
            if element <= minheap[j]:
                minheap.insert(j+1,element)
                inserted = True
                break
        if not inserted:
            minheap = [element] + minheap
    
    return minheap


def pop_heap(minheap):
    lenheap = len(minheap)
    middle = int(lenheap/2)
    if lenheap < 3:
        minheap.pop(middle)
        return minheap
    if lenheap == 3:
        if minheap[0] < minheap[2]:
            return [minheap[2],minheap[0]]
        return [minheap[0],minheap[2]]
    middle = int(lenheap/2)
    if len(minheap)%2 == 0:
        # popping will bring left child to the middle
        # make sure left child is smaller before popping
        if (minheap[middle-1] > minheap[middle+1]):
            minheap[middle] = minheap[middle+1]
            minheap[middle+1] = minheap[middle-1]
            minheap[middle-1] = minheap[middle]
        shiftee_pos = middle + 1
        neighbor_pos = middle + 2
        while ( neighbor_pos < lenheap and minheap[shiftee_pos] > minheap[neighbor_pos] ):
            temp = minheap[shiftee_pos]
            minheap[shiftee_pos] = minheap[neighbor_pos]
            minheap[neighbor_pos] = temp
            neighbor_pos += 1
            shiftee_pos += 1

    else:
        # popping will bring right child to the "middle"
        # make sure right child is smaller before popping
        if (minheap[middle+1] > minheap[middle-1]):
            minheap[middle] = minheap[middle+1]
            minheap[middle+1] = minheap[middle-1]
            minheap[middle-1] = minheap[middle]
        shiftee_pos = middle - 1
        neighbor_pos = middle - 2
        while (neighbor_pos>=0 and minheap[shiftee_pos] > minheap[neighbor_pos]):
            temp = minheap[shiftee_pos]
            minheap[shiftee_pos] = minheap[neighbor_pos]
            minheap[neighbor_pos] = temp
            neighbor_pos -= 1
            shiftee_pos -= 1

    minheap.pop(middle)
    return minheap

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        totalCost=0
        originalsize = len(costs)
        originalk = k
        candidatesremoved = 0
        firstsegment = costs[:candidates]
        overlap = (2*candidates - originalsize)
        if overlap < 0:
            overlap=0
        ls_startindex = originalsize+overlap-candidates
        lastsegment = costs[ls_startindex:]
        firstsegment = make_minheap(firstsegment)
        remainder=costs[candidates:ls_startindex]
        # print(f"first segment heaped: {firstsegment}")
        lastsegment = make_minheap(lastsegment)
        # print(f"last segment heaped: {lastsegment}")
        remainingsize = originalsize

        while(k>0):
            lenfirst = len(firstsegment)
            if lenfirst == 0:
                firstsegment = [100000]
                lenfirst = 1
            lenlast = len(lastsegment)
            if lenlast == 0:
                lastsegment = [100000]
                lenlast = 1
            middlefirst= int(lenfirst/2)
            middlelast=int(lenlast/2)
            # print(f"first segment heaped: {firstsegment}")
            # print(f"last segment heaped: {lastsegment}")
            if lastsegment[middlelast] < firstsegment[middlefirst]:
                hired = lastsegment[middlelast]
                lastsegment = pop_heap(lastsegment)
                if(len(remainder) > 0):
                    heap_addendum = remainder[-1]
                    remainder = remainder[:-1]
                    lastsegment = insert_to_minheap(lastsegment,heap_addendum)

            else:
                hired = firstsegment[middlefirst]
                firstsegment = pop_heap(firstsegment)
                if(len(remainder) > 0):
                    heap_addendum = remainder[0]
                    remainder = remainder[1:]
                    firstsegment = insert_to_minheap(firstsegment,heap_addendum)
                    
            totalCost += hired
            k -= 1
        return totalCost














# class Solution:
#     def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#         totalCost=0
#         originalsize = len(costs)
#         originalk = k
#         candidatesremoved = 0
#         while(k>0):
#             firstsegment = costs[:candidates]
#             ls_max_startindex = candidates if candidates > len(costs)-candidates else len(costs)-candidates
#             lastsegment = costs[ls_max_startindex:]
#             consideration = firstsegment + lastsegment
#             notconsidered = costs[candidates:len(costs)-candidates]
#             # print(f"calculating min on {consideration}")
#             totalCost+=min(consideration)
#             # print(min(consideration))
#             if min(consideration) in firstsegment:
#                 firstsegment.remove(min(consideration))
#                 # print(f"first segment: {firstsegment}")
#             else:
#                 lastsegment.remove(min(consideration))
#                 # print(f"last segment: {lastsegment}")
#             candidatesremoved += 1
#             costs = firstsegment + notconsidered
#             idealcostslen = originalsize - candidatesremoved
#             currentcostlen = len(costs)
#             costs += lastsegment[currentcostlen-idealcostslen:]
#             # print(costs)
#             k-=1

#         return totalCost
        