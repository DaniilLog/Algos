import sys
from collections import deque

res = []

class Node:
    def __init__(self, data):
        self.data = data
        self.par = None
        self.left = None
        self.right = None
        self.height = -1
        self.id = 0
        self.next = None


def build_tree(root):
    if (root.left != None):
        build_tree(root.left)
    if (root.right != None):
        build_tree(root.right)
    fix_height(root)


def height_right(root):
    if (root.right == None):
        return 0
    return root.right.height


def height_left(root):
    if (root.left == None):
        return 0
    return root.left.height


def fix_height(root):
    root.height = max(height_left(root), height_right(root)) + 1


def get_balance(root):
    r = 0
    l = 0
    if (root.right != None):
        r = root.right.height
    if (root.left != None):
        l = root.left.height
    return r - l


def rotate_tree(node, side):
    u = None
    if (side == 'left'):
        if node is None or node.right is None:
            return node
        parent = node.par
        right = node.right
        right_left = right.left
        if parent:
            if parent.right == node:
                parent.right = right
            else:
                parent.left = right
        right.par = parent
        right.left = node
        node.par = right
        node.right = right_left
        if right_left:
            right_left.par = node

        fix_height(node)
        fix_height(right)
        return right
    else:
        if node is None or node.left is None:
            return node
        parent = node.par
        left = node.left
        left_right = left.right
        if parent:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left
        left.par = parent
        left.right = node
        node.par = left
        node.left = left_right
        if left_right:
            left_right.par = node
        fix_height(node)
        fix_height(left)
        return left


def getMax(root):
    if (root == None):
        return root
    while root.right != None:
        root = root.right
    return root


def blnc(root):
    fix_height(root)
    balance = get_balance(root)
    if balance > 1:
        if get_balance(root.right) < 0:
            root.right = rotate_tree(root.right, 'right')
        return rotate_tree(root, 'left')

    elif balance < -1:
        if get_balance(root.left) > 0:
            root.left = rotate_tree(root.left, 'left')
        return rotate_tree(root, 'right')

    return root


def delete(root, key):
    if root == None:
        return root

    elif key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:

        if root.left is None and root.right is None:
            return None
        if root.left == None:
            root = root.right
            return blnc(root)

        temp = getMax(root.left)
        root.data = temp.data
        root.left = delete(root.left, temp.data)

    return blnc(root)


def printBST(root, n):
    global res
    queue = deque()
    queue.append((root, (-1, -1)))

    while queue:
        u, v = queue.popleft()
        if (v[0] >= 0 and v[1] >= 0):
            res[v[0]][v[1]] = len(res) + 1
        if (u == None):
            continue
        tmp = [0, 0, 0]
        tmp[0] = u.data
        res.append(tmp)
        cur = len(res)
        if (u.left != None):
            queue.append((u.left, (cur - 1, 1)))
        if (u.right != None):
            queue.append((u.right, (cur - 1, 2)))


sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
input = sys.stdin.readline
n = int(input())

root = []
for i in range(n + 10):
    root.append(Node(0))
for i in range(n):
    k, l, r = map(int, input().split())
    root[i + 1].data = k
    if (l):
        root[i + 1].left = root[l]
        root[l].par = root[i + 1]
    if (r):
        root[i + 1].right = root[r]
        root[r].par = root[i + 1]

val = int(input())

build_tree(root[1])
root[1] = delete(root[1], val)

printBST(root[1], n)
sys.stdout.write(str(len(res)) + "\n")
n = len(res)
for i, j, k in res:
    sys.stdout.write(str(i) + ' ' + str(j) + ' ' + str(k) + '\n')
