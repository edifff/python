class Stack:
    def __init__(self):
        self.stack=[]
    def push(self, el):
        self.stack.append(el)
    def pop(self):
        if len(self.stack)==0:
            return None
        return self.stack.pop()


stack=Stack()

for ch in input().strip().split():
    if ch== "+":
        stack.push(stack.pop()+stack.pop())
    elif ch== "-":
        el1, el2=stack.pop(), stack.pop()
        stack.push(el2-el1)
    elif ch== '*':
        stack.push(stack.pop() * stack.pop())
    else:
        stack.push(int(ch))
print(stack.pop())