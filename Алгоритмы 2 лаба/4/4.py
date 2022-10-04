class node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.size = None


class binTree:

    def __init__(self):
        self.root = None

    def search(self, data, root):
        if root is None or data == root.key:
            return root
        if data < root.key:
            if root.left is not None:
                return self.search(data, root.left)
            return root
        if root.right is not None:
            return self.search(data, root.right)
        return root

    def insert(self, data):
        if self.root is None:
            self.root = node()
            self.root.key = data
            self.root.size = 1
        else:
            t = self.search(data, self.root)
            if t.key == data:
                return
            elif data < t.key:
                t.left = node()
                t.left.key = data
                t.left.parent = t
                t.left.size = 1
            else:
                t.right = node()
                t.right.key = data
                t.right.parent = t
                t.right.size = 1
            while t is not None:
                t.size += 1
                t = t.parent

    def kMax(self, root, k):
        if root.left is None:
            s = 0
        else:
            s = root.left.size
        if k == s + 1:
            return root.key
        if k < s + 1:
            return self.kMax(root.left, k)
        return self.kMax(root.right, k-s-1)


f = open('input.txt', 'r')
o = open("output.txt", "w")
L = f.readlines()
T = binTree()
for i in L:
    com, x = i.split()
    if com == '+':
        T.insert(int(x))
    else:
        o.write(str(T.kMax(T.root, int(x))) + "\n")