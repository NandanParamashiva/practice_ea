#!/usr/bin/python

class BSTree:
    def __init__(self, data = -1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def minimumBST(root):
    if root == None:
        print 'Something went wrong'
        return None
    if root.left == None:
        return root
    return minimumBST(root.left)

def delete(root, data):
    if root == None:
        return None
    if data < root.data:
        root.left = delete(root.left, data)
        return root
    elif data > root.data:
        root.right = delete(root.right, data)
        return root
    else:
        #found node to delete
        if root.left == None and root.right == None:
            return None
        elif root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            # Has both children
            # Copy min of right child to root.data
            # and delete the min of right child
            # Note: min will never has left child
            # Hence it will fall to category 2 above
            minimum  = minimumBST(root.right)
            root.data = minimum.data
            root.right = delete(root.right, minimum.data)
            return root

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
    A = (15,6,99,33,7,42,9,3,11,86,110,105,111)
    print A
    root = BstAdd(None, A)
    print 'displaying preorder BST'
    display(root)
    delete(root, 99)
    print 'After delete'
    display(root)



if __name__=='__main__':
    main()