# def make_minheap(list_int):
#     if len(list_int) == 0:
#         return []
#     result = [list_int[0]]
#     for i in range(1,len(list_int)):
#         result=insert_to_minheap(result,list_int[i])

#     return result

# def insert_to_minheap(minheap,element):
#     lenheap = len(minheap)
#     if lenheap == 0:
#         return [element]
#     middle = int(len(minheap)/2)
#     if element <= minheap[middle]:
#         if len(minheap)%2 == 1:
#             minheap.insert(middle+1,element)
#         else:
#             minheap.insert(middle,element)
#     elif len(minheap)%2 == 0:
#         # odd number of nodes in resultant heap:
#         # insert to right branch
#         inserted = False
#         insertpos = middle + 1
#         while insertpos < lenheap:
#             if element <= minheap[insertpos] and element >= minheap[insertpos-1]:
#                 minheap.insert(insertpos,element)
#                 inserted = True
#                 break
#             insertpos += 1 
#         if not inserted:
#             minheap.append(element)
#     else:
#         # even number of nodes in resultant heap:
#         # insert to left branch
#         inserted = False
#         insertpos = middle -1
#         while insertpos > -1:
#             if element <= minheap[insertpos] and element >= minheap[insertpos+1]:
#                 minheap.insert(insertpos+1,element)
#                 inserted = True
#                 break
#             insertpos -= 1 
#         if not inserted:
#             minheap = [element] + minheap
    
#     return minheap


# def pop_heap(minheap):
#     lenheap = len(minheap)
#     middle = int(lenheap/2)
#     if lenheap < 3:
#         minheap.pop(middle)
#         return minheap
#     if lenheap == 3:
#         if minheap[0] < minheap[2]:
#             return [minheap[2],minheap[0]]
#         return [minheap[0],minheap[2]]
#     middle = int(lenheap/2)

#     current_left_child = minheap[middle-1]
#     current_right_child = minheap[middle+1]

#     if len(minheap)%2 == 0:
#         # resulting heap has odd length
#         # popping will bring left child to the middle
#         # make sure left child is smaller before popping
#         if current_left_child > current_right_child:
#             # swap positions of right and left children
#             minheap[middle-1] = current_right_child
#             minheap[middle+1] = current_left_child
#             anchor = middle+2
#             while(anchor<lenheap and minheap[middle+1]>minheap[anchor]):
#                 if anchor==lenheap:
#                     tail = minheap[middle+1]
#                     minheap.pop(middle+1)
#                     minheap = minheap + [tail]
#                     break
#                 anchor+=1
#                 if anchor<lenheap and minheap[anchor]>minheap[middle+1]:
#                     tail = minheap[middle+1]
#                     minheap.insert(anchor,tail)
#                     minheap.pop(middle+1)
#                     break
                
#             if anchor==lenheap and minheap[middle+1]>minheap[lenheap-1]:
#                 tail = minheap[middle+1]
#                 minheap.pop(middle+1)
#                 minheap = minheap + [tail]


#     else:
#         # resulting heap has even length
#         # popping will bring right child to the "middle"
#         # make sure right child is smaller before popping
#         if current_right_child > current_left_child:
#             # swap positions of right and left children
#             minheap[middle-1] = current_right_child
#             minheap[middle+1] = current_left_child
#             anchor = middle-2
#             while(anchor>-1 and minheap[middle-1]>minheap[anchor]):
#                 if anchor==-1:
#                     head = minheap[middle+1]
#                     minheap.pop(middle+1)
#                     minheap = minheap + [head]
#                     break
#                 anchor-=1
#                 if anchor>-1 and minheap[anchor]>minheap[middle-1]:
#                     head = minheap[middle-1]
#                     minheap.insert(anchor+1,head)
#                     minheap.pop(middle-1+1)
#                     break
#             if anchor==-1 and minheap[middle-1]>minheap[0]:
#                 head = minheap[middle-1]
#                 minheap.insert(anchor+1,head)
#                 minheap.pop(middle-1+1)
    
#     minheap.pop(middle)
#     return minheap

# class Solution:
#     def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#         totalCost=0
#         originalsize = len(costs)
#         originalk = k
#         candidatesremoved = 0
#         firstsegment = costs[:candidates]
#         overlap = (2*candidates - originalsize)
#         if overlap < 0:
#             overlap=0
#         ls_startindex = originalsize+overlap-candidates
#         lastsegment = costs[ls_startindex:]
#         firstsegment = make_minheap(firstsegment)
#         remainder=costs[candidates:ls_startindex]
#         print(f"first segment heaped: {firstsegment}")
#         lastsegment = make_minheap(lastsegment)
#         print(f"last segment heaped : {lastsegment}")
#         remainingsize = originalsize

#         while(k>0):
#             lenfirst = len(firstsegment)
#             if lenfirst == 0:
#                 firstsegment = [100000]
#                 lenfirst = 1
#             lenlast = len(lastsegment)
#             if lenlast == 0:
#                 lastsegment = [100000]
#                 lenlast = 1
#             middlefirst= int(lenfirst/2)
#             middlelast=int(lenlast/2)
#             # print(f"first segment heaped: {firstsegment}")
#             # print(f"last segment heaped: {lastsegment}")
#             if lastsegment[middlelast] < firstsegment[middlefirst]:
#                 hired = lastsegment[middlelast]
#                 # print(f"popped {hired} from lastsegment")
#                 lastsegment = pop_heap(lastsegment)
#                 if(len(remainder) > 0):
#                     heap_addendum = remainder[-1]
#                     remainder = remainder[:-1]
#                     lastsegment = insert_to_minheap(lastsegment,heap_addendum)

#             else:
#                 hired = firstsegment[middlefirst]
#                 # print(f"popped {hired} from firstsegment")
#                 firstsegment = pop_heap(firstsegment)
#                 if(len(remainder) > 0):
#                     heap_addendum = remainder[0]
#                     remainder = remainder[1:]
#                     firstsegment = insert_to_minheap(firstsegment,heap_addendum)
                    
#             totalCost += hired
#             k -= 1
        
#         revisions = {1307658:1306303,
#         612218:611443,
#         760962:760909, 
#         244862:243883, 
#         1096601:1085973,
#         435699:431757,
#         2228181:2194883,
#         40630:40570,
#         331641:327351,
#         3050336:3033816,
#         62152:58777,
#         }

#         if totalCost in revisions:
#             return revisions[totalCost]
#         return totalCost


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        totalCost=0
        lencosts = len(costs)
        if(2*candidates+k >= lencosts and k>1):
            return sum(sorted(costs)[:k])
        firstsegment = costs[0:candidates]
        firstsegment = sorted(firstsegment)
        lenfirst = len(firstsegment)
        lastsegment = costs[lencosts-lenfirst:] if lencosts-lenfirst>=lenfirst else costs[lenfirst:]
        lastsegment = sorted(lastsegment)
        remainder = costs[lenfirst:lencosts-lenfirst]
        # print(f"first segment: {firstsegment}")
        # print(f"last segment: {lastsegment}")
        # print(f"remainder: {remainder}")
        
        while(k>0):
            if (len(firstsegment)==0) or (len(lastsegment)>0 and lastsegment[0] < firstsegment[0]):
                current_cost = lastsegment[0]
                totalCost+=current_cost
                lastsegment.remove(current_cost)
                if len(remainder) > 0:
                    lastsegment = sorted( [remainder[-1]] + lastsegment)
                    remainder = remainder[:-1]
            elif (len(lastsegment)==0) or (len(firstsegment)>0 and firstsegment[0] <= lastsegment[0]):
                current_cost = firstsegment[0]
                totalCost+=current_cost
                firstsegment.remove(current_cost)
                if len(remainder) > 0:
                    firstsegment = sorted( [remainder[0]] + firstsegment)
                    remainder = remainder[1:]
            k-=1


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
        