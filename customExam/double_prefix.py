class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.rank = 1
        self.val = '0'
        self.root = False

from double_prefix_testy import runtests

def addWord(T,word):
    n = len(word)
    i=0
    while i<n:
        if(word[i] == '0'):
            if(T.left is None):
                T.left = Node()
                T.left.parent = T
                T = T.left
            else:
                T.left.rank+=1
                T = T.left
        if(word[i] == '1'):
            if(T.right is None):
                T.right = Node()
                T.right.val ='1'
                T.right.parent = T
                T = T.right
            else:
                T.right.rank+=1
                T = T.right
        i+=1   
res = []

def makeStr(T):
    s = T.val
    while not T.parent.root:
        T = T.parent
        s = T.val + s
    global res
    res.append(s)



def throughTree(T):
    if T is None or T.rank == 1:
        return
    throughTree(T.left)
    throughTree(T.right)
    if((T.left == None or T.left.rank ==1) and (T.right == None or T.right.rank ==1) and T.rank >= 2):
        makeStr(T)
    return


def double_prefix(L):
    global res
    res = []
    root = Node()
    root.root = True
    for w in L:
        addWord(root,w)
    throughTree(root.left)
    throughTree(root.right)
    return res


#double_prefix(['00111', '0010001', '00001', '0101111', '0001000', '0100010', '001011', '0010010'])



runtests(double_prefix)