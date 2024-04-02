class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0


n = int(input())
ls = list(map(int, input().split()))

st = Stack()
ind = 1
cnt = []
coun = 1
for i in ls:
    if i == ind:
        st.push(i)
        cnt.append((1, coun))
        coun = 0
        while st.top() == ind:
            coun += 1
            st.pop()
            ind += 1
        cnt.append((2, coun))
        coun = 1
    else:
        st.push(i)
        coun += 1

if not st.empty():
    print(0)
else:
    print(len(cnt))
    for i in cnt:
        print(*i)
