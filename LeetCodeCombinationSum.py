def increasingSequenceGenerator(minimum,maximum,elements,targetSum):
    output = []
    if elements==2:
        for i in range(minimum,maximum):
            j = targetSum - i
            if j<=i:
                break
            if j>maximum:
                continue
            output.append([i,j])
        return output
    for i in range(minimum,maximum):
        aux=increasingSequenceGenerator(i+1,maximum,elements-1,targetSum-i)
        for seq in aux:
            output.append([i]+seq)
    return output

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = increasingSequenceGenerator(1,9,k,n)
        print(output)
        return output