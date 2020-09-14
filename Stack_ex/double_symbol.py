"""用栈判断给定的字符串里括号，中括号，大括号是否成对出现
以下这几种表示法是对的： () [] {} ([{}])
以下这几种表示法是错的： (] [} ([{]})
"""

from myapp.structure import Stack


def isdouble(string: str) -> bool:
    """判断给定字符串的括号、中括号、大括号是否成对出现"""
    s = Stack()

    for each in string:
        if each in "([{":  # 遍历每一个字符，将开括号存入栈中
            s.push(each)
        elif each in ")]}":
            if s.isEmpty():  # 遍历到右扩号时，栈中必然有一个左括号，如果此时栈为空则返回假
                return False
            elif not match(each, s):
                return False

    if not s.isEmpty():
        return False
    else:
        return True


def match(each, s):
    """判断符号是否对应匹配
    开括号与闭括号的对应索引肯定相同，
    如果不同则代表括号没有成对出现
    """
    open_symbol = ['(', '[', '{']
    close_symbol = [')', ']', '}']
    return open_symbol.index(s.pop()) == close_symbol.index(each)


if __name__ == '__main__':
    print(isdouble("test([)]"))
