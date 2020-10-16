class UnorderedList:
    """无序链表"""

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
