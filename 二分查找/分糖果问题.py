# 甲乙丙三人分糖果，甲分到的比总数的一半多2颗，乙分到的比剩下的一半多2颗，丙分到6颗，问糖果有多少颗


def canfinish(value):
    x = value / 2 + 2  # 甲
    y = (value - x) / 2 + 2  # 乙
    z = 6  # 丙
    return x + y + z


def candy():
    temp = list(range(1, 50))
    left = 0
    right = len(temp) - 1
    while left <= right:
        middle = left + (right - left) // 2
        value = canfinish(temp[middle])
        if value == temp[middle]:
            return temp[middle]
        elif value > temp[middle]:
            left = middle + 1
        elif value < temp[middle]:
            right = middle - 1


print(candy())
