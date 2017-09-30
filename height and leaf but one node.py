#!/usr/bin/python

class BSTree:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def htAndLastButOneNodeAlongHtPath(root):
    if root == None:
        return -1, None
    left_ht, left_node = htAndLastButOneNodeAlongHtPath(root.left)
    right_ht, right_node = htAndLastButOneNodeAlongHtPath(root.right)
    if left_ht >= right_ht:
        ht, node = left_ht+1, left_node
    else:
        ht, node = right_ht+1, right_node
    if ht == 1:
        node = root
    return ht, node

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
    print 'displaying preorder BST'
    display(root)
    ht, node = htAndLastButOneNodeAlongHtPath(root)
    print 'height=%d, last but one node=%d'%(ht, node.data)

if __name__=='__main__':
    main()