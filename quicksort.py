#! /usr/bin/python

def swap(A, i, j):
    A[i],A[j] = A[j],A[i]
    return

def partition(A, s, e):

    pivot = A[e]
    p = s
    i = s
    while i < e:
        if A[i] < pivot:
            swap(A, i, p)
            p += 1
        i += 1
    swap(A, e, p)
    return p

def qs(A, s, e):
    if s >= e:
        return
    p = partition(A, s, e)
    qs(A, s, p-1)
    qs(A, p+1, e)

def main():
    A = [9,3,1,6,0,2,4,10]
    qs(A, 0, len(A)-1)
    print A

if __name__ == '__main__':
    main()