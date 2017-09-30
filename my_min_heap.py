#!/usr/bin/python


class Myheap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def mydisplay(self):
        print self.arr

    def good_index(self, index):
        if (index > (self.size-1)) or (index < 0):
            return False
        return True

    def __get_leftchild_index__(self, index):
        if not self.good_index(index):
            return None

        l_child = (2 * index) + 1
        if l_child > (self.size-1):
            return None
        return l_child

    def __get_rightchild_index__(self, index):
        if not self.good_index(index):
            return None

        r_child = (2 * index) + 2
        if r_child > (self.size-1):
            return None
        return r_child

    def __get__parent_index__(self, index):
        p = (index - 1) / 2
        if not self.good_index(index):
            return None
        return p

    def __swap__(self, index1, index2):
        if not self.good_index(index1):
            print 'swap failed'
            return
        if not self.good_index(index2):
            print 'swap failed'
            return
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def heapifyup(self):
        cur_index = self.size - 1 #last element
        parent_index = self.__get__parent_index__(cur_index)
        while (parent_index > -1):
            if (self.arr[cur_index] < self.arr[parent_index]):
                self.__swap__(cur_index, parent_index)
            cur_index = parent_index
            parent_index = self.__get__parent_index__(cur_index)

    def heapifydown(self):
        cur_index = 0
        while (cur_index < self.size):
            l_index = self.__get_leftchild_index__(cur_index)
            r_index = self.__get_rightchild_index__(cur_index)

            if not l_index:
                return

            small_index = l_index
            if r_index and (self.arr[r_index] < self.arr[l_index]):
                small_index = r_index

            if self.arr[small_index] < self.arr[cur_index]:
                self.__swap__(cur_index, small_index)

            cur_index = small_index

    def myheappush(self, e):
        #raise exception if e is not a number
        self.arr.append(e)
        self.size += 1
        self.heapifyup()

    def myheappop(self):
        last_item = self.arr[0]
        last_index = self.size - 1

        if self.size < 0 :
            return None

        if last_index < 0:
            return None

        self.__swap__(last_index, 0)
        self.size -= 1
        self.heapifydown()
        return last_item

def main():
    print 'inside main'
    h = Myheap()
    l = [11, 9, 5, 6, 7, 1, 4]
    for i in l:
        h.myheappush(i)
    total = h.size
    for i in range(total):
        h.mydisplay()
        print 'element=%d, size=%d'%(h.myheappop(), h.size)
        h.mydisplay()
        print

if __name__=='__main__':
    main()