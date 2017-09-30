#!/usr/bin/python

class BSTree:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def BstAddHelper(root, node):
    tmp = root
    if tmp == None:
        return node
    if node.data <= tmp.data:
        root.left = BstAddHelper(tmp.left, node)
    else:
        root.right = BstAddHelper(tmp.right, node)
    return root
    '''if root == None:
        root = node
        return
    tmp = root
    while (tmp != None):
        prev = tmp
        if (node.data <= tmp.data):
            tmp = tmp.left
        else:
            tmp = tmp.right
    if (node.data <= prev.data):
        prev.left = node
    else:
        prev.right = node'''

def display(root):
    tmp = root
    if root == None:
        return
    print root.data
    display(tmp.left)
    display(tmp.right)



def BstAdd(root, A):
    for i in A:
        new_node = BSTree(i)
        BstAddHelper(root, new_node)
        #display(root)


def main():
    A = (1,6,3,7,1,9,33,1,86)
    print A
    root = BSTree()
    BstAdd(root, A)
    print 'displaying BST'
    display(root)

if __name__=='__main__':
    main()