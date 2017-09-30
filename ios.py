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


def mini(root):
    if root==None:
        return None
    while(root.left != None):
        root = root.left
    return root


#inorder successor
def ios(root, suc, data):
    if root==None:
        return None
    if root.data == data:
        if root.right!=None:
            return mini(root.right)
        else:
            return suc
    if data < root.data:
        return ios(root.left, root, data)
    else:
        return ios(root.right, suc, data)

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
    ios_of = 11
    print 'displaying ios of %d'%ios_of
    ios_node =  ios(root, None, ios_of)
    print ios_node.data




if __name__=='__main__':
    main()