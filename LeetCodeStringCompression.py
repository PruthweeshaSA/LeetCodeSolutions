class Solution:
    def compress(self, chars: List[str]) -> int:
        # dictionary = {}
        count = 1
        write_head = 1
        for read_head in range(1,len(chars)):
            if chars[read_head] == chars[read_head-1]:
                # increment count since we have encountered a consecutive character occurrence
                count += 1
                # we need to handle final character separately
                if read_head == len(chars) - 1:
                    # if we are reading the last character and it has a count > 1:
                    # we are writing the count at write head.
                    if count == 1:
                        break
                    count = str(count)
                    for char in count:
                        # print(char)
                        chars[write_head] = char
                        write_head += 1
            else:
                # if there is only one occurrence of character, skip writing the trivial count of 1 
                if count == 1:
                    # since there is only one occurrence of character, skip writing the trivial count of 1 
                    chars[write_head] = chars[read_head]
                    write_head += 1
                    continue
                # if count > 10: we need to write individual digits as strings
                count = str(count)
                for char in count:
                    chars[write_head] = char
                    write_head += 1
                # reset count back to 1 because we encountered a different character
                count = 1
                # append new character to output string at write head and increment write head
                chars[write_head] = chars[read_head]
                write_head += 1
        
        chars = chars[:write_head+1]
        return write_head




        