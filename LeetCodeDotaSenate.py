class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if 'R' not in senate:
            return "Dire"
        elif 'D' not in senate:
            return "Radiant"
        while(True):
            i=0
            while i<len(senate):
                member = senate[i]
                if member == 'R':
                    if 'D' in senate[i+1:]:
                        senate = senate[:i]+senate[i:].replace('D','',1)
                        i+=1
                        continue
                    elif 'D' in senate[:i]:
                        senate = senate.replace('D','',1)
                        continue
                    else:
                        return "Radiant"
                else:
                    if 'R' in senate[i+1:]:
                        senate = senate[:i]+senate[i:].replace('R','',1)
                        i+=1
                        continue
                    elif 'R' in senate[:i]:
                        senate = senate.replace('R','',1)
                        continue
                    else:
                        return "Dire"
                i+=1
            if 'R' not in senate:
                return "Dire"
            elif 'D' not in senate:
                return "Radiant"
            