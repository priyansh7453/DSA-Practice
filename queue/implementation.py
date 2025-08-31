class Queue:
    def __init__(self, size=100001):
        self.size = size
        self.arr = [-1] * size
        self.qfront = 0
        self.rear = 0

    # Check if queue is empty
    def isEmpty(self):
        return self.qfront == self.rear

    # Add element (enqueue)
    def enqueue(self, data):
        if self.rear == self.size:
            print("Queue is Full")
        else:
            self.arr[self.rear] = data
            self.rear += 1

    # Remove element (dequeue)
    def dequeue(self):
        if self.qfront == self.rear:
            return -1  # Queue empty
        else:
            ans = self.arr[self.qfront]
            self.arr[self.qfront] = -1
            self.qfront += 1

            # Reset queue if empty
            if self.qfront == self.rear:
                self.qfront = 0
                self.rear = 0
            return ans

    # Get front element
    def front(self):
        if self.qfront == self.rear:
            return -1  # Queue empty
        else:
            return self.arr[self.qfront]
        
        
    # Get size of queue
    def sizeOfQueue(self):
        return self.rear - self.qfront
    def display(self):
        if self.qfront == self.rear:
            print("Queue is empty")
        else:
            for i in range(self.qfront, self.rear):
                print(self.arr[i], end=" ")
            print()
            
# Example usage
if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()  # Output: 10 20 30
    print(q.dequeue())  # Output: 10
    print(q.front())    # Output: 20
    print(q.sizeOfQueue())  # Output: 2
    q.display()  # Output: 20 30
    