from trees import root

"""
Given a root node to a binary tree... 
    print out the values using DFS - recursively
    print out the values using DFS - iteratively
    print out the values using BFS
"""


def search(root):
    if not root:
        return
    print(root.val)
    search(root.left)
    search(root.right)


search(root)


def search(root):
    while root:
        print(root.value)
        root.left


"""
Given a root node to a binary tree... 
    return the values Preorder - recursively - [1, 2, 5, 6, 3, 7, 8]
    return the values Preorder - iteratively
    return the values Inorder - recursively - [5, 2, 6, 1, 7, 3, 8]
    return the values Inorder - iteratively
    return the values Postorder
"""


def solution_pre_rec(root):

    def search(root, stack):
        if not root:
            return False
        stack.append(root.val)
        return search(root.left, stack) or search(root.right, stack)

    stack = []
    if root:
        stack.append(root.val)
    search(root.left, stack)
    search(root.right, stack)
    print(stack)
    return stack


def solution_pre_iter(root):
    pass


def solution_in_rec(root):
    pass


def solution_in_iter(root):
    pass


def search(root, stack):
    if not root:
        return
    if root.left:
        search(root.left, stack)
    stack.append(root.val)
    if root.right:
        search(root.right, stack)
    return stack


stack = []
ans = search(root, stack)
print(ans)
