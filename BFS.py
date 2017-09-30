#!/usr/bin/python

class BSTree:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def BFS(root):
    q = []
    bkupq = []
    q.insert(0, root)
    while q:
        node = q.pop()
        if node.left:
            q.insert(0,node.left)
        if node.right:
            q.insert(0,node.right)
        print node.data
        bkupq.append(node)
    return bkupq



def BstAddHelper(root, node):
    if root == None:
        return node
    if node.data <= root.data:
        root.left = BstAddHelper(root.left, node)
    else:
        root.right = BstAddHelper(root.right, node)
    return root

def BstAdd(root, A):
    for i in A:
        new_node = BSTree(i)
        root = BstAddHelper(root, new_node)
    return root

def display(root):
    tmp = root
    if root == None:
        return
    print root.data
    display(tmp.left)
    display(tmp.right)

def main():
    A = (1,6,3,7,1,9,33,1,86)
    print A
    root = BstAdd(None, A)
    #print 'displaying preorder BST'
    #display(root)
    print 'displaying BFS'
    bkupq = BFS(root)
    #for i in bkupq:
    #    print i.data



if __name__=='__main__':
    main()