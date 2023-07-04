"""
快速排序
平均时间复杂度：O(lgn*n)
最好情况: O(lgn*n)
最坏情况: O(n²)
空间复杂度: O(1)
稳定性： 不稳定
排序方式：比较排序
排序逻辑：1.随机取数组一个数字，然后把数组按照这个数字，把小的放左边，大的放右边。
            然后左右部分再重复此操作，直到左右数字小于等于0.
"""
from typing import List


def quick_sort(arr: List):
    """
    快速排序
    :param arr: 待排序数组
    :return: 已排序数组
    """
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr: List, low: int, high: int):
    """
    快速排序
    :param arr: 待排序数组
    :param low: 数组最小索引
    :param high: 数组最大索引
    :return:
    """
    if low >= high:
        return

    mid = _partition(arr, low, high)
    _quick_sort(arr, low, mid - 1)
    _quick_sort(arr, mid + 1, high)


def _partition(arr: List, low: int, high: int):
    """
    分割数组
    :param arr: 带分割数组
    :param low: 数组最小索引
    :param high: 数组最大索引
    :return: 分割索引
    """
    # 分割元素
    param = arr[high]
    j = low
    for i in range(low, high):
        if arr[i] < param:
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[high], arr[j] = arr[j], arr[high]
    print(low, high, arr)
    return j


if __name__ == '__main__':
    my_arr = [4, 6, 2, 8, 9]
    print(quick_sort(my_arr))
