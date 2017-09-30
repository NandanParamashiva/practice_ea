#! /usr/bin/python

def merge(A, m, s, e , temp):
    l, lstart = s, s
    lend = m
    r, rstart = m+1, m+1
    i = 0
    rend = e
    while l <= lend and r <= rend:
        if A[l] < A[r]:
            temp[i] = A[l]
            l += 1
        else:
            temp[i] = A[r]
            r += 1
        i += 1
    while l <= lend:
        temp[i] = A[l]
        l += 1
        i += 1
    while r <= rend:
        temp[i] = A[r]
        r += 1
        i += 1
    return


def copy(src, dest, s):
    for i,elem in enumerate(src):
        dest[s+i] = elem

def ms(A, s, e):
    if s >= e:
        return
    m = s + ((e - s) / 2)
    ms(A, s, m)
    ms(A, m+1, e)
    temp = [0 for i in xrange(0,e-s+1)]
    merge(A, m, s, e, temp)
    copy(temp, A, s)


def main():
    A = [2,7,3,9,6,8,1,0,5]
    ms(A, 0, len(A)-1)
    print A

if __name__ == '__main__':
    main()