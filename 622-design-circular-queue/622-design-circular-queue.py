class MyCircularQueue:

    class Node:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next
        
    def __init__(self, k: int):
        self.front = self.Node()
        self.rear = self.front
        if k == 1:
            self.front.next = self.front
            self.rear.next = self.rear
        else:        
            node = self.Node()
            self.rear.next = node
            for _ in range(k-2):
                node.next = self.Node()
                node = node.next
            node.next = self.rear

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear.val = value            
            self.rear = self.rear.next
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front.val = None
            self.front = self.front.next
            return True
        return False

    def Front(self) -> int:
        return self.front.val if self.front.val is not None else -1

    def Rear(self) -> int:
        if self.isEmpty():  return -1
        node = self.front
        while node.next != self.rear:
            node = node.next
        return node.val

    def isEmpty(self) -> bool:
        return self.front.val is None

    def isFull(self) -> bool:
        return self.rear == self.front and self.front.val


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()