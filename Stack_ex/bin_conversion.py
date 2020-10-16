from myapp.structure.Stack import Stack


def bin_convert(digit: int, num: int) -> str:
    """将digit转换为num进制并输出，
    二进制：除二取余
    八进制：除八取余
    十六进制：除十六取余
    """
    s = Stack()
    temp = "0123456789ABCDEF"
    result = ''

    while digit != 0:
        s.push(digit % num)
        digit = digit // num

    while not s.isEmpty():
        result += temp[s.pop()]

    return result


if __name__ == '__main__':
    print(f"255 二进制 -->{bin_convert(255, 2)}")
    print(f"255 八进制 -->{bin_convert(255, 8)}")
    print(f"255 十六进制 -->{bin_convert(255, 16)}")
