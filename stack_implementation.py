class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        top = self.stack.pop()
        if top == self.max_stack[-1]:
            self.max_stack.pop()
        return top

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def peekMax(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]

    def popMax(self):
        if not self.max_stack:
            return None
        max_val = self.max_stack[-1]
        buffer = []
        while self.top() != max_val:
            buffer.append(self.pop())
        self.pop()
        while buffer:
            self.push(buffer.pop())
        return max_val
    
max_stack = MaxStack()
max_stack.push(5)
max_stack.push(1)
max_stack.push(5)
print(max_stack.top()) 
print(max_stack.popMax())  
print(max_stack.top())  
print(max_stack.peekMax())  
print(max_stack.pop())
print(max_stack.top())  
