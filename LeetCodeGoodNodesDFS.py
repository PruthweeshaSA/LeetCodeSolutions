# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def BFS(nodeList):
#     newList = []
#     while(len(nodeList)>0):
#         node = nodeList.pop(0)
#         if node is not None:
#             # print(node.val)
#             newList.append(node.left)
#             newList.append(node.right)
#     if len(newList) > 0:
#         BFS(newList)

def DFS(node,count,maximum):
    if node.val >= maximum: # Haan Bhai 5 >= 4 sahi hai
        maximum = node.val # Maximum = 5
        count += 1 # Count 1 Ho gaya
    lcount = DFS(node.left,0,maximum) if node.left is not None else 0 # 3 waale node ka lcount 1 hai
    rcount = DFS(node.right,0,maximum) if node.right is not None else 0 # 3 waale node ka rcount 2 hai
    count += lcount + rcount # 1 + 1+ 2 = 4 ho gaya
    return count # 4 return ho raha hai from root-node

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is not None:
            return DFS(root,0,root.val) # (3 waala node, 0, 3)
        return 0
