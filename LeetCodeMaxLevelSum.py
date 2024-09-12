# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def BFS_max(currentGen:List['TreeNode'],maximum:int,max_level:int,level:int) -> int:
    sum_level=0
    nextGen=[]
    for node in currentGen:
        if node.left is not None:
            nextGen.append(node.left)
        if node.right is not None:
            nextGen.append(node.right)
        sum_level+=node.val
    if sum_level > maximum:
        maximum = sum_level
        max_level = level
    if len(nextGen)>0:
        max_level = BFS_max(nextGen,maximum,max_level,level+1)
    return max_level

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        return BFS_max([root],root.val,1,1)
        