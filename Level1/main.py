class MinMaxStack:
    def __init__(self):
        self.stack = []  # Main stack to store numbers
        self.min_stack = []  # Stack to track min values
        self.max_stack = []  # Stack to track max values

    def push(self, x):
        self.stack.append(x)

        # Update min stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

        # Update max stack
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
            self.max_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None  # If stack is empty

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None  # If stack is empty

    def getMax(self):
        if self.max_stack:
            return self.max_stack[-1]
        return None  # If stack is empty

# Example Usage
s = MinMaxStack()
s.push(5)
s.push(2)
s.push(8)
s.push(1)

print(s.getMin())  # Output: 1
print(s.getMax())  # Output: 8

s.pop()  # Removes 1
print(s.getMin())  # Output: 2
print(s.getMax())  # Output: 8
