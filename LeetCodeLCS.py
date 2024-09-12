class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcsl = [ [0] * (len(text2)+1) ]

        for i in range (len(text1)):
            lcsl += [ [0] * (len(text2)+1) ]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if i==0 or j==0:
                    lcsl[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    lcsl[i][j] = 1 + lcsl[i-1][j-1]
                else:
                    lcsl[i][j] = max(lcsl[i-1][j],lcsl[i][j-1])

        return lcsl[-1][-1]