def list_sum(obj: list) -> int:
    """递归求给定列表的元素之和"""
    if len(obj) == 1:
        return obj[0]
    return list_sum(obj[1:]) + obj[0]


if __name__ == '__main__':
    print(list_sum([1, 3, 5, 7, 9]))
