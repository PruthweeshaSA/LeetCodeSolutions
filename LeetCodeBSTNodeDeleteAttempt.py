# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getInOrderSuccessor(root):
    if root.right is not None:
        successor = root.right
        while(successor.left is not None):
            successor = successor.left
        return successor
    elif root.left is not None:
        return root.left
    return None

def BST_Search(root,key):
    if root is None:
        return None
    if root.val == key:
        print (f"found at root:{root.val} == {key}")
        return root
    while root is not None:
        if key == root.val:
            return root
        if key < root.val:
            if root.left is None:
                return None
            root=root.left
        else:
            if root.right is None:
                return None
            root=root.right
    return None

def advancedSearch(root,key):
    if root is None:
        return (None,0)
    if root.val == key:
        return (root,0)
    while(root is not None):
        if root.right is not None and root.right.val == key:
            return (root, 1)
        if root.left is not None and root.left.val == key:
            return (root, -1)
        if key < root.val:
            if root.left is None:
                return (None,0)
            root=root.left
        else:
            if root.right is None:
                return (None,0)
            root=root.right
    return (None,0)

def BST_SearchRoute(root,key):
    route = "  "
    if root is None:
        return None
    if root.val == key:
        return route
    while root is not None:
        if key < root.val:
            if root.left is None:
                return None
            root=root.left
            route = route + "L"
        else:
            if root.right is None:
                return None
            root=root.right
            route = route + "R"
    return route

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = BST_Search(root,key)
        parent = BST_SearchRoute(root,key)
        if root is not None and root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

        print(parent)
        if node is not None:
            if node.left is None and node.right is None:
                op_tuple = advancedSearch(root,key)
                parent=op_tuple[0]
                if op_tuple[1] == -1:
                    node = parent.left
                    parent.left = None
                elif op_tuple[1] == 1:
                    node = parent.right
                    parent.right = None
                    return root
            replacer = getInOrderSuccessor(node)
            print(f"inorder successor: {replacer}")
            if replacer is None and node is not None:
                node.val = 'null'
                node.right = None
                node.left = None
            elif root.right is not None and root.right.val == replacer.val:
                node.val = replacer.val
                node.right = replacer.right
                print(replacer.val)
            elif replacer is not None:
                node.val = replacer.val
                print(replacer.val)
                if replacer.left is None and node.right is not None and node.right.val == replacer.val:
                    node.right = replacer.right
                else:
                    replacer.val = 'null'
                replacer.right = None
                replacer.left = None
                replacer = None
            elif node.right is None and node.left is None:
                return None

        elif root is not None and root.val == key:
            root.val = 'null'
        elif root is not None:
            return root
        else:
            return None
        return root


        