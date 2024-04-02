class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def push(self, item):
        self.stack.append(item)

    def empty(self):
        return len(self.stack) == 0


    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[0]



number = int(input())
stack = Stack()

for _ in range(number):
    string = input()



    if string[0] == "1":
        gtr = int(string.split()[-1])
        if stack.empty():
            stack.push((gtr, gtr))
        else:
            a, c = stack.top()
            stack.push((gtr, min(c, gtr)))


    elif string[0] == "2":
        stack.pop()
    elif string[0] == "3":
        a, c = stack.top()
        print(c)