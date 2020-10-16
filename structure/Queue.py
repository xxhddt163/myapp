class Queue:
    """构建队列"""

    def __init__(self):
        self.item = []

    def enqueue(self, item):
        """向队尾增加元素"""
        self.item.insert(0, item)

    def dequeue(self):
        """向队首弹出数据"""
        return self.item.pop()

    def isEmpty(self):
        """判断队列是否为空"""
        return self.item == []

    def size(self):
        """返回队列的元素个数"""
        return len(self.item)
