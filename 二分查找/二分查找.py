# 二分查找可能出现的三种情况、
# 1、无重复元素的序列
# 2、有重复元素的序列返回左边界索引
# 3、有重复元素的序列返回右边界索引
"""若目标值不在序列中则返回 -1
算法可视化地址：https://www.cs.usfca.edu/~galles/visualization/Search.html
"""


class Binary_Search:
    def __init__(self, nums: list, target: int):
        self.nums = nums
        self.target = target

    def binary_search(self):
        """标准二分查找
        给定列表无重复值
        """
        left = 0  # 左边界
        right = len(self.nums) - 1  # 右边界

        while left <= right:
            middle = left + (right - left) // 2  # 中间点
            if self.nums[middle] == self.target:  # 中间的数恰好为目标值
                return middle
            elif self.nums[middle] > self.target:  # 中间的数大于目标值 减小右边界
                right = middle - 1
            elif self.nums[middle] < self.target:  # 中间的数3小于目标值 增加左边界
                left = middle + 1
        return -1  # 当目标值不在列表中

    def left_bound(self):
        """给出左边界的索引
        给定的列表有重复值
        """
        left = 0
        right = len(self.nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if self.nums[middle] == self.target:
                right = middle - 1  # 注意这里跟标准的二分查找变化了，由于是找左边界，所以减小右边界的值
            elif self.nums[middle] < self.target:
                left = middle + 1
            elif self.nums[middle] > self.target:
                right = middle - 1

        if left >= len(self.nums) or self.nums[left] != self.target:
            return -1
        return left  # 在有重复的元素时返回左边界是返回left

    def right_bound(self):
        """给出右边界的索引
        给定的列表有重复值
        """
        left = 0
        right = len(self.nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if self.nums[middle] == self.target:
                left = middle + 1  # 注意这里跟标准的二分查找变化了，由于是找右边界，所以增大左边界的值
            elif self.nums[middle] > self.target:
                right = middle - 1
            elif self.nums[middle] < self.target:
                left = middle + 1
        if right < 0 or self.nums[right] != self.target:
            return -1
        return right  # 在有重复的元素时返回right


if __name__ == '__main__':
    b = Binary_Search([1, 2, 3, 4, 5], 2)
    print(b.binary_search())
    b = Binary_Search([1, 2, 3, 4, 5], 9)
    print(b.binary_search())

    b = Binary_Search([1, 2, 2, 2, 2, 3, 4, 5], 2)
    print(b.left_bound())
    b = Binary_Search([1, 2, 2, 2, 2, 3, 4, 5], 3)
    print(b.left_bound())
    b = Binary_Search([1, 2, 2, 3, 4], 2)
    print(b.left_bound())

    b = Binary_Search([1, 2, 2, 2, 2, 3, 4, 5], 2)
    print(b.right_bound())
