import heapq

ls = [5, 7, 9, 1, 3]
print('Original list:', ls)

# convert list into heap (heap property)
heapq.heapify(ls)

print('The modified list converted into heap:', ls)

# push element into heap
heapq.heappush(ls, 4)
print('The modified heap:', ls)

# pop the smallest element
print(heapq.heappop(ls))


"""
INSERT AND BUBBLE UP (key k):  // runtime: O(log(n))
stick k at the end of last level
bubble-up k until heap property is restored (i.e. key of k's parent <= k)
"""

"""
EXTRACT-MIN AND BUBBLE DOWN:  // runtime: O(log(n))
delete root
move last leaf to be new root
iteratively bubble-down until heap property is restored
    [always swap with smaller child!]
"""

"""
parent(i): i//2
left child: 2*i
right child: 2*i + 1
MIN-HEAP PROPERTY: 
    for every node i
        ls[parent(i) <= ls[i]
"""

# Source: http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html

class Heap:
    def __int__(self):
        self.list = [0] # an empty binary heap has a single zero as the first element
        self.size = 0  # keep track of current size

    def bubble_up(self, i):
        # until we get to the top of the tree i.e. element 0 we initialized
        while i//2 > 0:  # while parent > 0
            # if newly added item is less than parent then swap it with its parent
            if self.list[i] < self.list[i//2]:
                self.list[i], self.list[i//2] = self.list[i//2], self.list[i]
            i //= 2  # make child the parent for further iterations

    def insert(self, item):
        self.list.append(item)
        self.size += 1
        self.bubble_up(self.size)

    def bubble_down(self, i):
        while 2*i <= self.size:
            min_ch = self.min_child(i)
            if self.list[i] > self.list[min_ch]:
                self.list[i], self.list[min_ch] = self.list[min_ch], self.list[i]
            i = min_ch  # recover i for further iterations

    def min_child(self, i):
        if 2*i + 1 > self.size:  # right child >  size (special condition)
            minimum = 2*i  # left child
        else:
            if self.list[2*i] < self.list[2*i + 1]:  # left child < right child
                minimum = 2*i  # left child
            else:
                minimum = 2*i + 1  # right child
        return minimum

    def extract_min(self):
        min_element = self.list[1]  # first element of heap (second element of list as first is 0)
        self.list[1] = self.list[self.size]
        self.size -= 1
        self.list.pop()
        self.bubble_down(1)
        return min_element

    def build_min_heap(self, ls):
        i = len(ls) // 2
        self.size = len(ls)
        self.list = [0] + ls[:]
        while i > 0:
            self.bubble_down(i)
            i -= 1


h = Heap()
h.build_min_heap([9, 5, 6, 2, 3])
#           9                       2
#       6       5       =>      3       5
#   2      3                  6    9
print('*'*20)
print(h.extract_min())
print(h.extract_min())
print(h.extract_min())
print(h.extract_min())
