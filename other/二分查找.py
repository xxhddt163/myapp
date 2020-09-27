class Binary_Search:
    def __init__(self, nums: list, target: int):
        self.nums = nums
        self.target = target

    def binary_search(self):
        """标准状态下的二分查找
        类型：所给定的数组没有含有重复的元素
        """
        left = 0  # 最左边的边界点
        right = len(self.nums) - 1  # 最右边的边界点
        # 代码中 left + (right - left) / 2 就和 (left + right) / 2 的结果相同，但是有效防止了 left 和 right 太大直接相加导致溢出
        while left <= right:
            middle = left + (right - left) // 2  # 中间点

            if self.nums[middle] == self.target:  # 由于列表是无重复元素的，当中间元素恰好为target
                return middle
            elif self.nums[middle] > self.target:  # 中间的数大于目标数，右边界为middle - 1
                right = middle - 1
            elif self.nums[middle] < self.target:  # 中间的数小于目标数，左边界为middle + 1
                left = middle + 1
        return -1  # target不存在number中时left必然大于right 跳出循环

    def left_bound(self):
        """当nums的元素有重复值时，返回左边界的索引"""
        left = 0
        right = len(self.nums) - 1
        while left <= right:
            middle = left + (right - left) // 2

            if self.nums[middle] == self.target:  # 由于nums中有重复元素，当中间数为target时继续减少右边界
                right = middle - 1
            elif self.nums[middle] > self.target:
                right = middle - 1
            elif self.nums[middle] < self.target:
                left = middle + 1

        if left >= len(self.nums) or self.nums[left] != self.target:
            return -1
        return left

    def right_bound(self):
        """返回右边界的索引"""
        left = 0
        right = len(self.nums) - 1
        while left <= right:
            middle = left + (right - left) // 2

            if self.nums[middle] == self.target:
                left = middle + 1
            elif self.nums[middle] > self.target:
                right = middle - 1
            elif self.nums[middle] < self.target:
                left = middle + 1

        if right >= len(self.nums) or self.nums[right] != self.target:
            return -1
        return right


if __name__ == '__main__':
    b = Binary_Search([1, 2, 3, 4, 5], 6)
    print(b.binary_search())
    b = Binary_Search([1, 2, 2, 2, 3, 4, 5], 2)
    print(b.left_bound())
    print(b.right_bound())
