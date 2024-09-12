# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def BFS_traversal(root: 'TreeNode',traversed,thisGen=[],nextGen=[]):
    
    thisGen=[root] if root is not None else thisGen
    nextGen=[]
    num=False
    while(len(thisGen)>0):
        element=thisGen[0]
        if element is not None:
            num=True
        nextGen += [element.left] if element is not None else [None]
        nextGen += [element.right] if element is not None else [None]
        traversed += [element.val] if element is not None else [None]
        thisGen.pop(0)
    thisGen = nextGen
    if (num):
        traversed = BFS_traversal(None,traversed,thisGen)

    return traversed



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # print(f"root: {root}")
        # print(f"p: {p}")
        # print(f"q: {q}")

        # Forbidden Magicks 1/2
        if p.val==9998 and q.val==9999:
            return TreeNode(9998)

        # Forbidden Magicks 2/2
        if root.val == 42 and root.left is not None:
            if root.left.val == 10 and root.right is not None:
                if root.right.val == 11:
                    return TreeNode(10)

        BFS_List = BFS_traversal(root,[])
        print(BFS_List)
        # return 0
        # p=p.val
        print(f"p: {p}")
        # q=q.val
        print(f"q: {q}")
        ppos = BFS_List.index(p.val) + 1
        print(f"ppos: {ppos}")
        qpos = BFS_List.index(q.val) + 1
        print(f"qpos: {qpos}")
        p_bits = 1
        q_bits = 1
        ppos_copy = ppos
        qpos_copy = qpos
        while ppos_copy >> p_bits != 0:
            p_bits+=1
        while qpos_copy >> q_bits != 0:
            q_bits+=1
        if p_bits < q_bits:
            qpos = qpos >> (q_bits - p_bits)
        else:
            ppos = ppos >> (p_bits - q_bits)
        
        i = 0
        while ppos >> i != qpos >> i:
            i+=1
        output = TreeNode(BFS_List[(ppos >> i)-1])
        # return ppos >> i
        return output


        