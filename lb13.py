def enqueue(data):
   queue.insert(0,data)

#Removing the front element from the queue
def dequeue():
   if len(queue)>0:
      return queue.pop()
   return ("Queue Empty!")

#To display the elements of the queue
def display():
   print("Elements on queue are:");
   for i in range(len(queue)):
      print(queue[i])

# executable code
if __name__=="__main__":
   queue=[]
   enqueue(5)
   enqueue(6)
   enqueue(9)
   enqueue(5)
   enqueue(3)
   print("Popped Element is: "+str(dequeue()))
   display()
