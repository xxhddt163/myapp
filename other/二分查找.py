def binary_search(list1: list, key: int) -> int or bool:
    """通过二分查找检测key是否在list1中"""
    list1 = sorted(list1)  # 将列表按从小到大排序
    begin = 0  # 最左边的指针指向起点索引
    end = len(list1) - 1  # 最右边的指针指向终点索引
    while begin <= end:
        middle = begin + (end - begin) // 2  # 中间点
        if key > list1[middle]:
            begin = middle + 1
        elif key < list1[middle]:
            end = middle - 1
        else:
            return middle
    return False


print(binary_search([3, 2, 1, 5, 7, 10, 12], 4))
