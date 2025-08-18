class TwoStack:
    def __init__(self, size):
        self.size = size           # Total size of the array
        self.arr = [None] * size   # Shared array for both stacks
        self.top1 = -1             # Top pointer for Stack 1, starts at left end
        self.top2 = size           # Top pointer for Stack 2, starts at right end

    # Push in Stack 1 (works from left to right)
    def push1(self, num):
        # Check if space exists
        if self.top2 - self.top1 > 1:
            self.top1 += 1
            self.arr[self.top1] = num
        else:
            print("Stack Overflow for Stack 1.")

    # Push in Stack 2 (works from right to left)
    def push2(self, num):
        # Check if space exists
        if self.top2 - self.top1 > 1:
            self.top2 -= 1
            self.arr[self.top2] = num
        else:
            print("Stack Overflow for Stack 2.")

    # Pop from Stack 1 (remove and return top of Stack 1)
    def pop1(self):
        if self.top1 >= 0:
            ans = self.arr[self.top1]
            self.top1 -= 1
            return ans
        else:
            print("Stack Underflow for Stack 1.")
            return -1

    # Pop from Stack 2 (remove and return top of Stack 2)
    def pop2(self):
        if self.top2 < self.size:
            ans = self.arr[self.top2]
            self.top2 += 1
            return ans
        else:
            print("Stack Underflow for Stack 2.")
            return -1

# Example Usage
ts = TwoStack(5)

ts.push1(10)
ts.push2(20)
ts.push1(30)
ts.push2(40)
ts.push1(50)   # This will fill available space

print(ts.pop1())  # Output: 50
print(ts.pop2())  # Output: 40
print(ts.pop1())  # Output: 30
print(ts.pop2())  # Output: 20
