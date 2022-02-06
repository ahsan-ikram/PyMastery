import abc

"""
Challenge: Implement a Queue using two Stacks
Queue = FIFO
Stack = LIFO
"""


class Xifo(metaclass=abc.ABCMeta):

    def __init__(self):
        self.buffer = []
        self.head = 0
        self.tail = 0

    def peek(self):
        return self.buffer[self.head]

    def is_empty(self):
        return True if len(self.buffer) == 0 else False

    def __str__(self):
        return str(self.buffer)


class Queue(Xifo):

    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        self.buffer.append(item)
        self.tail += 1

    def dequeue(self):
        item = self.buffer[self.head]
        self.buffer.remove(item)
        self.tail -= 1
        return item


class Stack(Xifo):

    def __init__(self):
        super().__init__()

    def push(self, item):
        self.buffer.append(item)
        self.head += 1

    def pop(self):
        item = self.buffer[self.head - 1]
        self.buffer.remove(item)
        self.head -= 1
        return item


class QueueViaStacks:

    def __init__(self):
        self._s1 = Stack()
        self._s2 = Stack()

    def enqueue(self, item):
        while not self._s1.is_empty():
            self._s2.push(self._s1.pop())
        self._s1.push(item)
        while not self._s2.is_empty():
            self._s1.push(self._s2.pop())

    def dequeue(self):
        return self._s1.pop()


class StackViaQueues:
    def __init__(self):
        self._q1 = Queue()
        self._q2 = Queue()

    def push(self, item):
        while not self._q1.is_empty():
            self._q2.enqueue(self._q1.dequeue())
        self._q1.enqueue(item)
        while not self._q2.is_empty():
            self._q1.enqueue(self._q2.dequeue())

    def pop(self):
        return self._q1.dequeue()


def main():
    n = 10
    stack = StackViaQueues()
    queue = QueueViaStacks()
    for i in range(n):
        stack.push(i)
        print(f'Stack push operation with item = {i}')
        queue.enqueue(i)
        print(f'Queue enqueue operation with item = {i}')

    for i in range(n):
        print(f'Stack pop operation with item = {stack.pop()}')

    for i in range(n):
        print(f'Queue dequeue operation with item = {queue.dequeue()}')


if __name__ == '__main__':
    main()
