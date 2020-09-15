def bin_convert(number: int, num: int) -> str:
    """递归算法实现整数到任意进制的转换"""
    conversting = '0123456789ABCDEF'
    if number < num:
        return conversting[number]
    return bin_convert(number // num, num) + conversting[number % num]


if __name__ == '__main__':
    print(bin_convert(255, 16))
