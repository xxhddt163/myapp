def gcd(p: int, q: int) -> int:
    """递归算法求2数最大公约数
    使用欧几里得算法求最大公约数

    2个数p、q 如果除数为0 则这两个数的最大公约数为被除数，
    如果除数不为0 则用两数相除，取余，将除数作为被除数，余数
    作为除数继续除，直到除数为0，则返回p为两数的最大公约数
    """
    if q == 0:
        return p
    else:
        return gcd(q, p % q)


print(gcd(153, 17))
