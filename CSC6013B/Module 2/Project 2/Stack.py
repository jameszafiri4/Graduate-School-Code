'''
This file will include a class that implements a stack

It will be able to add and remove items from the stack

It can also return the size, check if it's empty, and return the top

'''

class Stack:
    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
