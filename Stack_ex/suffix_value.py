from myapp.structure.Stack import Stack


def suffix_value(string: str) -> int:
    """求后缀表达式的值"""
    s = Stack()

    string = string.split()
    for each in string:
        if each.isdigit():
            s.push(int(each))
        else:
            s.push(math(s, each))

    return int(s.pop())


def math(s, each):
    """求2个数的算术结果"""
    value2 = s.pop()
    value1 = s.pop()
    if each == '+':
        return value1 + value2
    elif each == '-':
        return value1 - value2
    elif each == '*':
        return value1 * value2
    else:
        return value1 / value2


if __name__ == '__main__':
    print(suffix_value("5 5 5 / +"))