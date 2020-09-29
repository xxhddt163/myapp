# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
#
#  珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后
# 这一小时内不会再吃更多的香蕉。
#
#  珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
#
#  返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
#
#
#
#
#
#
#  示例 1：
#
#  输入: piles = [3,6,7,11], H = 8
# 输出: 4
#
#
#  示例 2：
#
#  输入: piles = [30,11,23,4,20], H = 5
# 输出: 30
#
#
#  示例 3：
#
#  输入: piles = [30,11,23,4,20], H = 6
# 输出: 23
#
#
#
#
#  提示：
#
#
#  1 <= piles.length <= 10^4
#  piles.length <= H <= 10^9
#  1 <= piles[i] <= 10^9
#
#  Related Topics 二分查找
#  👍 99 👎 0


def min_time(plies: list, hour: int) -> int:
    left = 1  # 最低一个小时吃1个香蕉
    right = len(plies)  # 最高一个小时吃max(plies)个香蕉
    while left <= right:
        middle = left + (right - left) // 2  # 取一个中间速度测试
        if canfinish(plies, middle, hour):
            right = middle - 1  # 二分查找寻找左边界值，减少右边边界
        else:
            left = middle + 1
    return left  # 由于需要输出最小速度，刚好符合二分查找取左边界的最小值


def canfinish(plies, speed, hour):
    """测试所给的速度能否在给定时间内吃完香蕉"""
    time = 0
    for each in plies:  # 分别便利plies中的每个元素，计算该speed吃完所有香蕉总共需要多少小时
        time += check_time(each, speed)
    return time <= hour  # 所需时间小于给定时间则返回True


def check_time(n, speed):
    """计算n个香蕉以speed的速度要吃多少小时
    比如吃8个香蕉给定速度为3那就需要
    8 // 3 == 2小时 + 1个小时"""
    return n // speed + (0 if n % speed == 0 else 1)


print(min_time([1, 2, 3, 4, 8], 10))
