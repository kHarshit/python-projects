class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s = Stack()
s.push(54)
s.push(45)
s.push('+')
print(s.size())
print(s.pop())
s.push(True)

while not s.is_empty():
    print(s.pop(), end=' ')
