from myapp.structure import Deque


def palcheck(string: str) -> bool:
    """判断给定字符串是否为回文字符串"""
    d = Deque()
    for each in string:
        d.addRear(each)

    while d.size() > 1:
        value1 = d.removeRear()  # 返回队列的最后一个元素
        value2 = d.removeFront()  # 返回队列的第一个元素
        if value1 != value2:
            return False

    return True


if __name__ == '__main__':
    print(palcheck("上海自来水来自海上"))
