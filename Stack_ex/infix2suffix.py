from myapp.structure import Stack


def infix2suffix(string: str) -> str:
    """中缀表达式转后缀表达式
    如：a * b + c * d -> ab*cd*+
    """
    constant = "0123456789abcdefghijklmnopqrstuvwxyz"
    s = Stack()
    result = []
    priority = {'/': 3, '*': 3, '-': 2, '+': 2, '(': 1}  # 表示各种符号的优先级
    string = string.lower().split()  # 将字符串转换成列表
    for each in string:
        if each in constant:  # 如果遍历的对象为常数，则直接将该值加入输出结果的列表中
            result.append(each)
        elif each == "(":  # 如果对象为左括号直接加入栈中
            s.push(each)
        elif each == ")":
            temp = s.pop()
            while temp != '(':  # 如果each为右括号，则将栈内的值一直弹出，直到弹出值为左括号为止
                result.append(temp)
        else:
            # 由于*/的优先级大于+-,当遍历到符号时判断栈顶的符号优先级是否大于each，
            # 如果大于则将栈顶的值弹出到列表中，直到栈顶的值得优先级小于each或者将栈弹空
            # 否则则将符号推入栈中
            while not s.isEmpty() and priority[s.peek()] >= priority[each]:
                result.append(s.pop())
            s.push(each)

    while not s.isEmpty():
        result.append(s.pop())

    return ''.join(result)  # 将列表转换成字符串输出


if __name__ == '__main__':
    print(infix2suffix('5 + 5 / 5'))
