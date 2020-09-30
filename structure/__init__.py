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


class Node:
    """链表的节点"""

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderList:
    """链表"""

    def __init__(self):
        self.head = None

    def add(self, item):
        """向链表表头添加元素"""
        temp = Node(item)  # 为链表先增加一个节点temp
        temp.setNext(self.head)  # 将下一个指向设置为表头
        self.head = temp  # 将表头设置为新增加的节点

    def size(self):
        """获取链表的节点个数"""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        """检查目标元素是否在链表内"""
        found = False
        current = self.head
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        """删除列表中的指定元素"""
        current = self.head  # 用来存放当前节点的指向
        previous = None  # 用来存放上一个节点的指向
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
