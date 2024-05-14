# class Stack():
#     def __init__(self):
#         self.elements=[]
        
#     def isEmpty(self):
#         return self.elements==[]
#     def push(self,new):
#         self.elements.append(new)
#     def pop(self):
#         self.elements.pop()
#     def showLast(self):
#         return (self.elements[len(self.elements)-1])
#     def size(self):
#         return len(self.elements)
    
# myStack=Stack()
# myStack.push(15)
# #print(myStack.isEmpty())
# myStack.push(12)
# #print(myStack.showLast())
# secondStack=Stack()
# secondStack.push(myStack.pop())
# secondStack.showLast()
class Stack():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def push(self, new):
        self.elements.append(new)

    def pop(self):
        if not self.isEmpty():  # Önce yığdın boş olup olmadığını kontrol et
            return self.elements.pop()
        else:
            return None  # Eğer yığın boşsa None döndür

    def showLast(self):
        if not self.isEmpty():  # Önce yığdın boş olup olmadığını kontrol et
            return self.elements[-1]
        else:
            return None  # Eğer yığın boşsa None döndür

    def size(self):
        return len(self.elements)

myStack = Stack()
myStack.push(15)
#print(myStack.isEmpty())
myStack.push(12)
myStack.push("Deereere")
#print(myStack.showLast())
secondStack = Stack()
secondStack.push(myStack.pop())
print(secondStack.showLast())
