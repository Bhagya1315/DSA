'''class stack:

    def __init__(self):
        self.stack = []

        #push
    def push(self,data):
        self.stack.append(data)

        #pop
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()
    #peak
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    #isEmpty
    def is_empty(self):
        return len(self.stack)==0

    #size
    def size(self):
        return len(self.stack)


s= stack()
s.push(10)
s.push(20)
s.push(30)

print("Top: ",s.peek())
print("Popped: ",s.pop())
print("Size: ",s.size())
print("Is Empty: ",s.is_empty())
'''

'''stack = []
#push
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after push: ",stack)
#pop
removed = stack.pop()
print("poped element: ",removed)
print("Stack after pop: ",stack)
#peek
top = stack[-1]
print("Top element: ",top)
#isempty
print("Is stack empty ? ", len(stack)==0)
#size
print("Stack size: ", len(stack))
'''

'''from collections import deque
stack = deque()
#push
stack.append(10)
stack.append(20)

print(stack)
#pop()
stack.pop()
print(stack)
#peek
print(stack[-1])

'''


#checking valid parenthesis
def isValid(s):
    stack =[]
    mapping={')':'(','}':'{',']':'['}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1]!= mapping:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)== 0
s=input("Enter a string of brackets: ")

if isValid(s):
    print("Valid parenthesis")
else:
    print("Invalid Parenthesis")




'''def isBalanced(s):
    stack =[]

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
s=input("Enter a string of brackets: ")

if isBalanced(s):
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")
'''

'''#Remove outer parntheses
#remove outer most parenthesis from every primitive string
#IDEA
-> Keep a counter(or stack)
->only add char's when inner levels


'''

'''def removeOuterParentheses(s):
    result = ''
    count = 0
    
    for ch in s:
        if ch == '(':
            if count>0:
                result += ch
            count+=1

        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s="(()())"
print(removeOuterParentheses(s))
'''






        
