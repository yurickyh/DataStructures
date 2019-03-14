import sys

class Stack:
    def __init__(self):
        self.n = 0
        self.bottom = None
        self.top = None
    
    def push(self, content):
        if(self.n == 0):
            new_node = Node(content, None)
            self.top = new_node
            self.bottom = new_node
        else:
            new_node = Node(content, self.top)
            self.top = new_node
        self.n += 1

    def pop(self):
        if(self.n <= 0):
            print("Impossible to pop because the stack don't have any element.")
        else:
            self.top = self.top.previous
            self.n -= 1
    
    def peek(self):
        if(self.n <= 0):
            print("Impossible to peek because the queue don't have any element.")
        else:
            print(self.top.content)

    def print_nodes(self):
        memory = []
        current_node = self.top
        for i in range(0, self.n):
            memory.append(current_node.content)
            current_node = current_node.previous
        for element in memory:
            print(element),
            print(" "),
        print("")
    
class Node:
    def __init__(self, content, previous):
        self.content = content
        self.previous = previous

def main():
    stack = Stack()
    stack.push(1)
    stack.push(10)
    stack.push(9)
    stack.push(5)
    stack.push(26)
    stack.push(8)
    stack.push(-1)
    stack.print_nodes()
    stack.pop()
    stack.peek()
    stack.pop()
    stack.print_nodes()

main()