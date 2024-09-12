class Solution:
    def decodeString(self, s: str) -> str:
        open_bracket_stack = []
        num_stashed = []
        num_ongoing = 0
        i=0
        while i<len(s):
            if s[i] == '[':
                open_bracket_stack.append(i)
                num_stashed.append(num_ongoing)
                num_ongoing = 0
            elif s[i] == ']':
                br_start_pos = open_bracket_stack.pop()
                reps = num_stashed.pop()
                length_of_num = len(str(reps))
                payload = s[br_start_pos+1:i]
                resultant_string = payload * reps
                i_skip = len(payload)*(reps-1) - length_of_num - 2
                head = s[0:br_start_pos-length_of_num]
                tail = s[i+1:]
                s = head + resultant_string + tail
                i+=i_skip
            elif s[i].isdigit():
                num_ongoing = num_ongoing*10 + int(s[i])
            i+=1
        return s
                

        