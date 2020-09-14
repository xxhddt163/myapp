class Stack:
    """构建栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        """判定栈是否为空"""
        return self.items == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.items)

    def peek(self):
        """返回栈顶的元素"""
        return self.items[-1]

    def push(self, item):
        """栈顶加入元素"""
        self.items.append(item)

    def pop(self):
        """栈顶弹出元素"""
        return self.items.pop()


class Queue:
    """构建队列"""

    def __init__(self):
        self.item = []

    def enqueue(self, item):
        """向队尾增加元素"""
        self.item.index(0, item)

    def dequeue(self):
        """向队首弹出数据"""
        return self.item.pop()

    def isEmpty(self):
        """判断队列是否为空"""
        return self.item == []

    def size(self):
        """返回队列的元素个数"""
        return len(self.item)
