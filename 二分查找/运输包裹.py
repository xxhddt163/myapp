# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
#
#  传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
#
#  返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
#
#
#
#  示例 1：
#
#  输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# 输出：15
# 解释：
# 船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
# 第 1 天：1, 2, 3, 4, 5
# 第 2 天：6, 7
# 第 3 天：8
# 第 4 天：9
# 第 5 天：10
#
# 请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (1
# 0) 是不允许的。
#
#
#  示例 2：
#
#  输入：weights = [3,2,2,4,1,4], D = 3
# 输出：6
# 解释：
# 船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
# 第 1 天：3, 2
# 第 2 天：2, 4
# 第 3 天：1, 4
#
#
#  示例 3：
#
#  输入：weights = [1,2,3,1,1], D = 4
# 输出：3
# 解释：
# 第 1 天：1
# 第 2 天：2
# 第 3 天：3
# 第 4 天：1, 1
#
#
#
#
#  提示：
#
#
#  1 <= D <= weights.length <= 50000
#  1 <= weights[i] <= 500
#
#  Related Topics 数组 二分查找
#  👍 126 👎 0


"""船的最低载重为max(weight),最大载重量为sum(weight)"""


def min_weight(weight: list, day: int) -> int:
    left = max(weight)  # 最小载重量
    right = sum(weight)  # 最大载重量
    while left <= right:
        middle = left + (right - left) // 2  # 中间载重量
        if canfinish(weight, day, middle):
            right = middle - 1
        else:
            left = middle + 1
    return left


def canfinish(weight, days, cap):
    """计算指定载重量在days天内是否能将货物运完"""
    i = 0  # 用来记录列表索引号
    for day in range(days):
        max_cap = cap
        while max_cap - weight[i] >= 0:
            max_cap = max_cap - weight[i]
            i += 1
            if i == len(weight):
                return True
    return False


print(min_weight([1, 2, 3, 4, 5], 3))
