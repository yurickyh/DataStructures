import sys

class Queue:
    def __init__(self):
        self.n = 0
        self.last = None
        self.first = None

    def enqueue(self, content):
        if (self.n == 0):
            new_node = Node(content, None)
            self.last = new_node
            self.first = new_node
        else:
            new_node = Node(content, None)
            self.last.next = new_node
            self.last = new_node
        self.n += 1

    def dequeue(self):
        if(self.n <= 0):
            print("Impossible to dequeue because the queue don't have any element.")
        else:
            self.first = self.first.next
            self.n -= 1
    
    def peek(self):
        if(self.n <= 0):
            print("Impossible to dequeue because the queue don't have any element.")
        else:
            print(self.first.content)

    def print_nodes(self):
        current_node = self.first
        for i in range(0, self.n):
            print (current_node.content),
            print(" "),
            current_node = current_node.next
        print("")
        

class Node:
    def __init__(self, content, next_node):
        self.content = content
        self.next = next_node

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(10)
    queue.enqueue(3)
    queue.enqueue(39)
    queue.print_nodes()
    queue.peek()
    queue.dequeue()
    queue.print_nodes()

main()