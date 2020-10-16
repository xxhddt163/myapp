class OrderedList:
    """有序链表"""

    def __init__(self):
        self.head = None

    def add(self, item):
        """向链表表头添加元素"""
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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
        stop = False
        while current is not None and not found and not stop:
            if current.getData() > item:
                stop = True
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
