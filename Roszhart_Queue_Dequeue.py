#create a class for the Nodes

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#create a class for Queue, starts off empty
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

#check for empty queue, otherwise adds data 
    def Enqueue(self,data):
        if self.rear is None:
            self.front = self.rear = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next

#again check for empty queue, then makes the next node the new front
    def Dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        else:
            to_return = self.front.data
            self.front = self.front.next
            return to_return

#checks whether the queue is empty, t/f
    def IsEmpty(self):
        return self.front is None

#size function to determine size of queue
    def Size(self):
        count = 0
        current = self.front
        while(current):
            count += 1
            current = current.next
        return count

#returns the data of the front node
    def Front(self):
        return self.front.data

#returns the data of the last node
    def Rear(self):
        return self.rear.data
    
q = Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
print ('Is empty? ',q.IsEmpty())
print ('Size :',q.Size())
print ('Front :',q.Front())
print ('Rear :',q.Rear())
q.Dequeue()
q.Dequeue()
q.Dequeue()
q.Dequeue()
q.Dequeue()
print ('Is empty? ',q.IsEmpty())
print ('Size :',q.Size())