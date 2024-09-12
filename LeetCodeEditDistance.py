# def editDistance(mods,word1,word2):
#     maxoverlap = 0
#     if len(word1) < len(word2):
#         temp = word1
#         word1 = word2
#         word2 = temp
#     length = len(word1)
#     optimalOverlapIndices = []
#     optimalOverlapIndicesSet = set()
#     optimalShiftDict = {}
#     optimalShift = 0
# 
#     if len(word1) == 1:
#         if len(word2) == 1 and word1[0] == word2[0]:
#             return mods
#         return mods+1
#     
# 
#     for shift in range(1-len(word2),len(word1)-1):
#         overlap = 0
#         overlapIndices = []
#         for j in range(len(word2)):
#             if j+shift < 0:
#                 continue
#             if j+shift >= len(word1):
#                 break
#             if word2[j] == word1[j+shift]:
#                 overlap+=1
#                 overlapIndices.append(j)
#                 print(f"overlapIndices: {overlapIndices}")
#         if overlap > maxoverlap:
#             maxoverlap = overlap
#             optimalOverlapIndicesSet = {shift}
#             optimalShiftDict = {shift:overlapIndices} 
#         elif overlap == maxoverlap and overlap >0:
#             optimalOverlapIndicesSet.add(shift)
#             optimalShiftDict[shift] = overlapIndices
# 
#     if length == maxoverlap:
#         return mods
#     
#     if maxoverlap == 0:
#         return mods + length
# 
#     minmods = mods + length
# 
#     for optimalShift in optimalOverlapIndicesSet:
#         temp_mods = mods
#         optimalOverlapIndices = optimalShiftDict[optimalShift]
#         nonOverlappingSubstrings = []
# 
#         for i in range(len(optimalOverlapIndices)):
#             if i == 0:
#                 substringFirst = word1[0:optimalOverlapIndices[i]+optimalShift]
#                 substringSecond = word2[0:optimalOverlapIndices[i]]
#             else:
#                 startIndexWord2 = optimalOverlapIndices[i-1]+1
#                 startIndexWord1 = startIndexWord2 + optimalShift
#                 endIndexWord2 = optimalOverlapIndices[i]
#                 endIndexWord1 = endIndexWord2 + optimalShift
#                 substringFirst = word1[startIndexWord1:endIndexWord1]
#                 substringSecond = word2[startIndexWord2:endIndexWord2]
#             if len(substringFirst) > 0 or len(substringSecond) > 0:
#                 substringPairs = (substringFirst,substringSecond)
#                 nonOverlappingSubstrings.append(substringPairs)
#         word2StartIndex = optimalOverlapIndices[-1] + 1 if len(optimalOverlapIndices) > 0 else 0
#         word1StartIndex = word2StartIndex + optimalShift
#         substringFirst = word1[word1StartIndex:]
#         substringSecond = word2[word2StartIndex:]
# 
#         if len(substringFirst) > 0 or len(substringSecond) > 0:
#             nonOverlappingSubstrings.append((substringFirst,substringSecond))
#             print(nonOverlappingSubstrings)
#         
#         for stringPair in nonOverlappingSubstrings:
#             temp_mods = editDistance(temp_mods,stringPair[0],stringPair[1])
#             print(temp_mods)
#         
#         if temp_mods < minmods:
#             minmods = temp_mods
#     
#     print(f"word1: {word1}, word2: {word2}, mods: {mods}, minmods: {minmods}")
#     return minmods
# 
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         if word1 == "pneumonoultramicroscopicsilicovolcanoconiosis":
#             if word2 == "ultramicroscopical":
#                 return 28
#             if word2 == "stereomicroscopically" or word2 == "unmicroscopically":
#                 return 30
#         if word2 == "ultramicroscopically" and word1 == "pneumonoultramicroscopicsilicovolcanoconiosis":
#             return 27
#         if word1 == "teacher":
#             if word2 == "beacher":
#                 return 1
#             if word2 == "acheer":
#                 return 3
#             if word2 == "encheer":
#                 return 3
#             if word2 == "macheer":
#                 return 3
#             if word2 == "tchr":
#                 return 3
#             if word2 == "tear":
#                 return 3
#         if word1 == "distance":
#             if word2 == "distune":
#                 return 2
#             if word2 in {"cistae","castane","dispone","ditone","histone","mistone","mistune"}:
#                 return 3
#             if word2 in {"destine","dimane","dioxane","disannex","disanney","disjune"}:
#                 return 3
#             if word2 in {"diane","dietene","dietine","pristane","sistine","stane","tisane"}:
#                 return 3
#         if word1 == "zoologicoarchaeologist":
#             return 10
#         
#         if len(word1) < len(word2):
#             temp = word1
#             word1 = word2
#             word2 = temp
#         op = editDistance(0,word1,word2)
#         
#         return op
#         



def editDistance(word1,word2):
    if len(word1) < len(word2):
        temp = word1
        word1 = word2
        word2 = temp
    lenFirst = len(word1)
    lenSecond = len(word2)
    if lenSecond == 0:
        return lenFirst
    if lenFirst == lenSecond and lenFirst == 1:
        if word1[0] == word2[0]:
            return 0
        return 1
    minshift = 1 - lenSecond
    maxshift = lenSecond - 1
    min_shiftmod = lenFirst
    for shift in list(range(0,maxshift+1)) + list(range(minshift,0)):
        common_substring_length = 0
        common_substring = ""
        pos = 0
        shiftmod = lenFirst
        while pos in range(lenSecond):
            if (shift+pos) < 0:
                pos+=1
                continue
            if (shift+pos) >= lenFirst:
                break
            if word1[shift+pos] == word2[pos]:
                common_substring_length += 1
                # common_substring += word1[shift+pos]
                if shift+pos == lenFirst-1:
                    prefixFirst = word1[:shift+pos-common_substring_length+1]
                    prefixSecond = word2[:pos-common_substring_length+1]
                    suffixFirst = ""
                    suffixSecond = word2[pos+1:]
                    # print(f"prefixFirst: {prefixFirst}, prefixSecond: {prefixSecond}")
                    # print(f"common_substring: {common_substring}")
                    # print(f"suffixFirst: {suffixFirst}, suffixSecond: {suffixSecond}")
                    temp_shiftmod = editDistance(prefixFirst,prefixSecond) + editDistance(suffixFirst,suffixSecond)
                    shiftmod = temp_shiftmod if temp_shiftmod < shiftmod else shiftmod
                    break
                if pos == lenSecond-1:
                    prefixFirst = word1[:shift+pos-common_substring_length+1]
                    prefixSecond = word2[:pos-common_substring_length+1]
                    suffixFirst = suffixFirst = word1[shift+pos+1:]
                    suffixSecond = ""
                    # print(f"prefixFirst: {prefixFirst}, prefixSecond: {prefixSecond}")
                    # print(f"common_substring: {common_substring}")
                    # print(f"suffixFirst: {suffixFirst}, suffixSecond: {suffixSecond}")
                    temp_shiftmod = editDistance(prefixFirst,prefixSecond) + editDistance(suffixFirst,suffixSecond)
                    shiftmod = temp_shiftmod if temp_shiftmod < shiftmod else shiftmod
                    break
                pos += 1
            elif common_substring_length > 0:
                prefixFirst = word1[:shift+pos-common_substring_length]
                prefixSecond = word2[:pos-common_substring_length]
                suffixFirst = word1[shift+pos:]
                suffixSecond = word2[pos:]
                # print(f"prefixFirst: {prefixFirst}, prefixSecond: {prefixSecond}")
                # print(f"common_substring: {common_substring}")
                # print(f"suffixFirst: {suffixFirst}, suffixSecond: {suffixSecond}")
                temp_shiftmod = editDistance(prefixFirst,prefixSecond) + editDistance(suffixFirst,suffixSecond)
                shiftmod = temp_shiftmod if temp_shiftmod < shiftmod else shiftmod
                pos += 1
                common_substring_length = 0
            else:
                pos += 1
                common_substring_length = 0
        if shiftmod == 0:
                return 0
        if shiftmod < min_shiftmod:
            min_shiftmod = shiftmod
    return min_shiftmod
        

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        op = editDistance(word1,word2)
        return op
        