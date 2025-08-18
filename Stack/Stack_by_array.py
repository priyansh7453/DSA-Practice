class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def push(self, element):
        if self.size - self.top > 1:
            self.top += 1
            self.arr[self.top] = element
        else:
            print("Stack OverFlow")

    def pop(self):
        if self.top >= 0:
            popped = self.arr[self.top]
            self.top -= 1
            return popped
        else:
            print("Stack UnderFlow")

    def peek(self):
        if self.top >= 0:
            return self.arr[self.top]
        else:
            print("Stack is Empty")
            return -1

    def is_empty(self):
        return self.top == -1

# Main program
st = Stack(5)
st.push(29)
st.push(43)
st.push(4)
st.push(22)
# st.push(43)
st.push(44)   # This will print "Stack OverFlow"
print(st.arr)
print(st.peek())
# st.pop()
print("the pop element ",st.pop())
print(st.peek())
st.pop()
print(st.peek())
st.pop()
print(st.peek())

if st.is_empty():
    print("Stack is Empty mere dost")
else:
    print("Stack is not Empty mere dost")


# Built-in Python stack demo using list
s = []
s.append(2)
s.append(3)
s.pop()
print("Printing top element", s[-1])
if len(s) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")
print("Size of stack is", len(s))
