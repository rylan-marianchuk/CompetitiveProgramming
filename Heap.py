import random

class Heap:
    def __init__(self, size = 20):
        self.length = size
        self.Heap = [None]*self.length
        self.insert_index = 0

    def getRight(self, i):
        return 2*i+1

    def getLeft(self, i):
        return 2*i+2

    def getParent(self, i):
        return (i-1) // 2

    def isEmpty(self):
        return self.Heap[0] == None

    def peek(self):
        if not self.isEmpty():
            return self.Heap[0]

    def update(self, node_i, new_prior):
        for i in range(self.length):
            if self.Heap[i] != None and self.Heap[i][0] == node_i:
                self.Heap[i][1] = new_prior
                return

    def enqueue(self, node, p):
        if self.insert_index == self.length - 1:
            raise Exception("Heap Full")

        self.Heap[self.insert_index] = (node, p)
        self.insert_index += 1
        self.bubbleUp(self.insert_index-1)


    def bubbleUp(self, index):
        if index == 0:
            return
        p = self.getParent(index)
        while index > 0 and self.Heap[index][1] < self.Heap[p][1]:
            # Swap
            self.Heap[index], self.Heap[p] = self.Heap[p], self.Heap[index]
            index = p
            p = self.getParent(index)

    def pop(self):
        if self.insert_index == 0:
            raise Exception("Heaep is empty")
        self.Heap[0] = self.Heap[self.insert_index-1]
        self.Heap[self.insert_index - 1] = None
        self.insert_index -= 1
        self.bubbleDown()



    def bubbleDown(self):
        node_swap = 0
        l = self.getLeft(node_swap)
        r = self.getRight(node_swap)
        while self.Heap[l] != None:
            # two children
            if self.Heap[r] != None:
                if self.Heap[l][1] < self.Heap[r][1]:
                    self.Heap[node_swap], self.Heap[l] = self.Heap[l], self.Heap[node_swap]
                    node_swap = l
                else:
                    self.Heap[node_swap], self.Heap[r] = self.Heap[r], self.Heap[node_swap]
                    node_swap = r
            # Else 1 child,
                # Check left
            l = self.getLeft(node_swap)
            r = self.getRight(node_swap)




