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
st = Stack()
cnt = 0
for c, i in enumerate(map(int, input().split())):
    if st.empty():
        st.push((i, 1))
        continue

    a, b = st.top()
    if a == i:
        st.push((i, b + 1))
    else:
        if b >= 3:
            cnt += b
            for _ in range(b):
                st.pop()
        a, b = st.top()
        if a == i:
            st.push((i, b + 1))
        else:
            st.push((i, 1))

while not st.empty():
    a, b = st.pop()
    if b >= 3:
        cnt += b

    for _ in range(b - 1):
        st.pop()
print(cnt)
