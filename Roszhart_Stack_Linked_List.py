#create the class for the stack

class Stack:
#define the Node class to contain an element, and a next for the link    
    class Node:
        __slots__ = 'element','next'
        
        def __init__(self, element, next):
            self.element = element
            self.next = next

#starts with no head and the size is 0, as there is no list to begin
    def __init__(self):
        self.head = None
        self.size = 0

#function to return the size of the stack
    def __len__(self):
        return self.size

#function to determine if the size is 0 then it is empty
    def is_empty(self):
        return self.size == 0

#push function to add in a new Node on top
    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size = self.size + 1

#pop function to pop out the top of the stack
    def pop(self):
        value = self.head.element
        self.head = self.head.next
        self.size = self.size - 1
        return value
    
#top function to show which element is the current head    
    def top(self):
        return self.head.element

#display function to be able to see what's happening
    def display(self):
        show = self.head
        while show:
            print(show.element, end=' > ')
            show = show.next
        print()

#example of pushing, popping, and displaying
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
print('Pop: ', s.pop())
s.display()
s.push(5)
s.display()
print('Top: ', s.top())