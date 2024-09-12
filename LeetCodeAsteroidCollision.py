# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         while(True):
#             lenlist = len(asteroids)
#             i = 0
#             while i in range(len(asteroids)-1):
#                 if asteroids[i] > 0 and asteroids[i+1] < 0:
#                     if asteroids[i] + asteroids[i+1] == 0:
#                         asteroids.pop(i)
#                         asteroids.pop(i)
#                         i -= 1 if i>0 else 0
#                     elif asteroids[i] > -asteroids[i+1]:
#                         asteroids.pop(i+1)
#                     else:
#                         asteroids.pop(i)
#                         i -= 1 if i>0 else 0
#                     continue
#                 i+=1
#             if lenlist == len(asteroids):
#                 break
#         return asteroids
# 



class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i in range(len(asteroids)-1):
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                if asteroids[i] + asteroids[i+1] == 0:
                    asteroids.pop(i)
                    asteroids.pop(i)
                    i -= 1 if i>0 else 0
                elif asteroids[i] > -asteroids[i+1]:
                    asteroids.pop(i+1)
                else:
                    asteroids.pop(i)
                    i -= 1 if i>0 else 0
                continue
            i+=1
        return asteroids