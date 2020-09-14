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

    def push(self, item):
        """栈顶加入元素"""
        self.items.append(item)

    def pop(self):
        """栈顶弹出元素"""
        self.items.pop()



