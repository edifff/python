class Item:
    def __init__(self, Key, Priority):
        self.Key = Key
        self.Priority = Priority
        self.l = None
        self.r = None

def split(t, Key):
    if not t:
        return None, None
    elif Key <= t.Key:
        l, t.l = split(t.l, Key)
        return l, t
    else:
        t.r, r = split(t.r, Key)
        return t, r

def merge(l, r):
    if not l or not r:
        return l if l else r
    elif l.Priority > r.Priority:
        l.r = merge(l.r, r)
        return l
    else:
        r.l = merge(l, r.l)
        return r

import heapq
import sys
class Heapnode:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
class AVLtree:
    def __init__(self):
        self.node = None
    def insert(self, elem):
        tree = self.node

        if tree == None:
            self.node = Heapnode()
            self.node.key = elem
            self.node.left = AVLtree()
            self.node.right = AVLtree()
        elif tree.key!=elem:
            if elem < tree.key:
                self.node.left.insert(elem)
            else:
                self.node.right.insert(elem)
    def search(self, x):
        result=-1
        while self.node!=None:
            if self.node.key >= x:
                result=self.node.key
                self = self.node.left
            else:
                self = self.node.right
        return result

n = int(input())
prev = None
root = AVLtree()
max_el = -1
for i in range(0, n):
    quest = list(sys.stdin.readline().split())
    if quest[0]=='+':
        elem = int(quest[1])
        if (prev != None) and (prev != -1):
            elem = (elem + prev) % 10**9
            prev = None
        if max_el ==-1 or elem >= max_el:
            max_el=elem
        root.insert(elem)#туть добавляем элемент в дерево
    else:
        if max_el>= int(quest[1]):
            prev = root.search(int(quest[1])) #функция выдает элемент
        else:
            prev = -1
        print(prev)
