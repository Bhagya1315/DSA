'''from collections import deque

dq = deque()

# Inserting elements
dq.append(10)
dq.append(20)
dq.appendleft(5)

print("Deque after insertion:", dq)

# Delete elements
dq.pop()
print("After pop:", dq)

dq.popleft()
print("After popleft:", dq)

# Add more elements
dq.append(30)
dq.append(40)

print("Final deque:", dq)

# Peek elements
print("Front Element:", dq[0])
print("Rear Element:", dq[-1])

#size
print("Size: ", len(dq))

'''






















'''
from collections import deque
def reverse(dq, k):
    stack = []

    for _ in range(k):
        stack.append(dq.popleft())

    while stack:
        dq.append(stack.pop())

    for _ in range(len(dq)-k):
        dq.append(dq.popleft())

    return dq

dq = deque([1, 2, 3, 4, 5])
k=3
print("Result: ",reverse(dq,k))
'''





'''from collections import deque
def is_palindrome(s):
    dq=deque(s)

    while len(dq) > 1:
        if dq.popleft()!=dq.pop():
            return False
    return True
s='madam'
print("Palindrome: ",is_palindrome(s))

'''






















