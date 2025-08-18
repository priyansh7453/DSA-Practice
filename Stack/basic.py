# write all operation of the stack 
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)   
    print("Stack after pushing 3 elements:", stack.stack)
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack after popping an element:", stack.stack)
    print("Is stack empty?", stack.is_empty())
    print("Current stack size:", stack.size())
# This code implements a basic stack with push, pop, peek, is_empty, and size methods.
# It demonstrates how to use the stack by pushing and popping elements, checking the top element,