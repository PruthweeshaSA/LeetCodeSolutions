# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def AddPaths(node, sumStack, currentBranchSum ,countPaths, targetSum):
    if node is None:
        return countPaths

    newBranchSum = currentBranchSum + node.val
    countPaths += sumStack[newBranchSum - targetSum] if (newBranchSum - targetSum) in sumStack else 0
    sumStack[newBranchSum] = 1 if newBranchSum not in sumStack else sumStack[newBranchSum] + 1
    countPaths += 1 if newBranchSum == targetSum else 0

    countPaths = AddPaths(node.left, sumStack|{},newBranchSum,countPaths,targetSum) if node.left is not None else countPaths
    countPaths = AddPaths(node.right, sumStack, newBranchSum,countPaths,targetSum) if node.right is not None else countPaths
    return countPaths

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return AddPaths(root, sumStack={}, currentBranchSum=0, countPaths=0, targetSum=targetSum)
        