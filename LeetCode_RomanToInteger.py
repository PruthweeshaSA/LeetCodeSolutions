class Solution:
    def romanToInt(self, s: str) -> int:
        arabic = {"I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        }
        integer = arabic[s[-1]]
        for i in range(len(s)-1):
            value = arabic[s[i]]
            integer += value if value >= arabic[s[i+1]] else (-value)
        return integer

