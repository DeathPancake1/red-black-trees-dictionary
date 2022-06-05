class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 1 means red


class RBTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fixInsert(node)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fixInsert(self, k):
        while k != self.root and k.parent.color == 1:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                elif k == k.parent.right:
                    k = k.parent
                    self.leftRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rightRotate(k.parent.parent)
                else:
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rightRotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                elif k == k.parent.left:
                    k = k.parent
                    self.rightRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.leftRotate(k.parent.parent)
                else:
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.leftRotate(k.parent.parent)
        self.root.color = 0

    def search(self, key):
        node = self.root
        while node != self.NULL:
            if node.val == key:
                return node
            elif key > node.val:
                node = node.right
            else:
                node = node.left

        return None

    def treeSize(self, node):
        if node != self.NULL:
            return 1 + self.treeSize(node.right) + self.treeSize(node.left)
        return 0

    def height(self, node):
        if node == self.NULL:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1


def loadDic(tree):
    f = open("EN-US-Dictionary.txt", "r")
    line = "x"
    while line:
        line = f.readline().rstrip('\n')
        tree.insertNode(line)

    f.close()


def dicSize(tree):
    return str(tree.treeSize(tree.root))


def lookupWord(tree, word):
    if tree.search(word) is None:
        return "No"
    return "Yes"


def insertWord(tree, word):
    if lookupWord(tree, word) == "Yes":
        print("ERROR: Word already in dictionary")
        return
    tree.insertNode(word)
    print("Word Inserted")


if __name__ == "__main__":
    dic = RBTree()
    dicSize(dic)
    flag = True
    while flag:
        c = input("1) Insert word\n2) Look up word\n3) Load Dictionary\n4) Print Size\n5) Print height\n0) Exit\n")
        if c == "1":
            inword = input("Word: ")
            insertWord(dic, inword)
            print("Size:", dicSize(dic), "words")
            print("Height:", dic.height(dic.root))
        elif c == "2":
            inword = input("Word: ")
            print(lookupWord(dic, inword))
        elif c == "3":
            loadDic(dic)
            print("Loaded with", dicSize(dic), "words!")
        elif c == "4":
            print("Size:", dicSize(dic), "words")
        elif c == "5":
            print("Height:", dic.height(dic.root))
        else:
            flag = False

