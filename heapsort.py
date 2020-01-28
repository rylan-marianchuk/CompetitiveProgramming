import math
import random
class Heap:
    a = []
    size = 0
    def __init__(self, s):
        self.a = [int(c) for c in s.split()]
        self.size = len(self.a)

    def getParentIndex(self, i):
        return (i - 1) // 2

    def insert(self, i):
        """
        Place the element at index i into the heap
        :param i:
        :return: void
        """
        p = self.getParentIndex(i)

        while p >= 0 and self.a[p] < self.a[i]:
            # swap
            temp = self.a[p]
            self.a[p] = self.a[i]
            self.a[i] = temp

            i = p
            p = self.getParentIndex(i)

        return


    def getFirstLeaf(self, size):
        """
        Given the size of the tree, return the index of the first leaf node
        :param size:
        :return:
        """

        return math.floor(size/2)


    def delete(self, e):
        """
        Remove the element e from the heap
        if e does not exists in the heap, throw an exception
        :param e:
        :return: void
        """
        self.size -= 1
        self.a[0] = self.a[self.size]
        index_of_firstL = self.getFirstLeaf(self.size)
        i = 0

        while i < index_of_firstL and (self.a[i] < self.a[i* 2 +1] or self.a[i] < self.a[i* 2 +2]):
            if self.a[i*2+2] < self.a[i* 2 +1]:
                c = 2*i+1
                # Swap
            else:
                # Swap other child
                c = 2 * i + 2

            temp = self.a[c]
            self.a[c] = self.a[i]
            self.a[i] = temp
            i = c


        return



    def peekMax(self):
        """
        :return: the max element with no further modifications
        """

        if len(self.a) > 0:
            return self.a[0]
        raise LookupError()



    def popMax(self):
        """
        Pop max element from heap and return it
        :return: the max element
        """
        if len(self.a) == 0:
            raise LookupError
        max_e = self.a[0]
        self.delete(max_e)
        return max_e



    def heapsort(self):
        """
        Implement heap sort on a
        :param a: the array to be sorted in place
        :return: a
        """
        for i in range(self.size):
            self.insert(i)
        for i in range(self.size - 1, 0, -1):
            self.a[i] = self.popMax()
        return self.a

l = " ".join([str(random.randint(0, 30)) for i in range(0, 24)])
h = Heap(l)
h.heapsort()
print(h.a)