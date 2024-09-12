# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getInOrderSuccessor(node):
    if node.right is not None:
        successor = node.right
        if successor.left is None:
            return (node,1,node.right)
        while(successor.left is not None):
            parent=successor
            successor = successor.left
        return (parent,-1,parent.left)
    elif node.left is not None:
        return (node,-1,node.left)
    else:
        return (None,0,None)

def advancedSearch(root,key):
    if root is None:
        return (None,0,None)
    if root.val == key:
        return (root,0,root)
    while(root is not None):
        if root.right is not None and root.right.val == key:
            return (root, 1,root.right)
        if root.left is not None and root.left.val == key:
            return (root, -1,root.left)
        if key < root.val:
            if root.left is None:
                return (None,0,None)
            root=root.left
        else:
            if root.right is None:
                return (None,0,None)
            root=root.right
    return (None,0,None)

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is not None and root.val == key:
            if root.right is None:
                if root.left is None:
                    return None
                return root.left
            if root.left is None:
                return root.right
        
        nodeParentTuple = advancedSearch(root,key)
        nodeParent = nodeParentTuple[0]
        node = nodeParentTuple[2]

        if nodeParentTuple[1] == 0 and nodeParent is not None:
            # key is root
            node = nodeParent
            successorParentTuple = getInOrderSuccessor(node)
            successorParent = successorParentTuple[0]
            successor = successorParentTuple[2]
            if successorParentTuple[1] == 0:
                # root is successor; only root node exists
                if successorParent is not None:
                    return root
                else:
                    return None
            if successorParentTuple[1] == -1:
                # root replacer is a left child:
                successorParent.left = None if successor.right is None else successor.right
                successor.left = root.left
                successor.right = root.right
                return successor
            if successorParentTuple[1] == 1:
                # root replacer is a right child
                successor.left = root.left
                return successor


        elif nodeParentTuple[1] == 0:
            return root

        elif nodeParentTuple[1] == 1:
            # node is right child
            successorParentTuple = getInOrderSuccessor(node)
            successorParent = successorParentTuple[0]
            successor = successorParentTuple[2]
            if successorParentTuple[1] == 0:
                # node has no successor: leaf node can be safely deleted
                nodeParent.right = None
            elif successorParentTuple[1] == 1:
                #successor is right child
                nodeParent.right = successor
                successor.left = node.left
            elif successorParentTuple[1] == -1:
                #successor is left child
                if node.right is None:
                    nodeParent.right = successor
                else:
                    successorParent.left = None if successor.right is None else successor.right
                    nodeParent.right = successor
                    successor.left = node.left
                    successor.right = node.right if node.val != successorParent.val else successor.right
                


        
        elif nodeParentTuple[1] == -1:
           # node is left child
            successorParentTuple = getInOrderSuccessor(node)
            successorParent = successorParentTuple[0]
            successor = successorParentTuple[2]
            if successorParentTuple[1] == 0:
                # node has no successor: leaf node can be safely deleted
                nodeParent.left = None
            elif successorParentTuple[1] == 1:
                #successor is right child
                nodeParent.left = successor
                successor.left = node.left if node.left is not None else successor.left
            elif successorParentTuple[1] == -1:
                #successor is left child
                nodeParent.left = successor
                successor.left = node.left if node.val != successorParent.val else successor.left
                successorParent.left = None if successor.right is None else successor.right
                successor.right = node.right
                
        
        return root