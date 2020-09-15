def pal_sum(num: int) -> int:
    """递归求1-num的和"""
    if num == 1:
        return num
    return pal_sum(num - 1) + num


if __name__ == '__main__':
    print(pal_sum(100))