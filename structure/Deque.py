class Deque:
    """双端队列"""

    def __init__(self):
        self.items = []

    def addFront(self, item):
        """在队首加入元素"""
        self.items.append(item)

    def removeFront(self):
        """弹出队首元素"""
        return self.items.pop()

    def addRear(self, item):
        """队尾加入元素"""
        self.items.insert(0, item)

    def removeRear(self):
        """队尾移除元素"""
        return self.items.pop(0)

    def isEmpty(self):
        """返回队列是否为空"""
        return self.items == []

    def size(self):
        """返回队列元素个数"""
        return len(self.items)
