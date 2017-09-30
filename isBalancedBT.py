#!/usr/bin/python

class BSTree:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def isBalancedBST(root):
    if root == None:
        return True, -1

    status_left, ht_left = isBalancedBST(root.left)
    status_right, ht_right = isBalancedBST(root.right)
    ht = max(ht_left, ht_right) + 1

    if (status_left == False or
        status_right == False):
        return False, ht

    diff = ht_left - ht_right
    if diff > 1 or diff < -1:
        print 'found imbalance at node=%d, ht_left=%d, ht_right=%d'%(root.data, ht_left, ht_right)
        return False, ht
    else:
        return True, ht


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
    display(tmp.left)
    print root.data
    display(tmp.right)

def main():
    A = (15,6,99,33,7,42,9,8,3,11,86,110,105,111)
    print A
    root = BstAdd(None, A)
    print 'displaying preorder BST'
    display(root)
    status, ht = isBalancedBST(root)
    print status,ht

if __name__=='__main__':
    main()