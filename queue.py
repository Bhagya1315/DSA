'''class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) ==0

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)


print("Queue: ",q.queue)
print("Dequeue: ",q.dequeue())
print("Pek: ",q.peek())
print("Size:",q.size())
print("Is empty: ", q.is_empty())
'''



from collections import deque
q = deque()
q.append(10)
q.append(20)
q.append(30)

print("Queue: ", q)

print("Deque: ", q.popleft())
print("Deque: ", q.popleft())

