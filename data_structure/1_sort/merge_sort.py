"""
归并排序
平均时间复杂度：O(lgn*n)
最好情况: O(lgn*n)
最坏情况: O(lgn*n)
空间复杂度: O(n)
稳定性： 稳定
排序方式：比较排序
排序逻辑：1.把待排序序列平均分为两组，然后再在每组进行归并排序。每分排序好之后，进行合并。
        终止条件是只剩下一个元素。
"""
from typing import List


def merge_sort(arr: List):
    """
    归并排序
    :param arr: 待排序数组
    :return: 排序好的数组
    """
    arr_len = len(arr)
    _merge_sort(arr, 0, arr_len)
    return arr


def _merge_sort(arr: List, low: int, high: int):
    """
    归并排序递归方法
    :param arr: 待排序数组
    :param low: 最小序列
    :param high: 最大序列
    :return:
    """
    if low + 1 >= high:
        return
    mid = low + (high - low) // 2
    _merge_sort(arr, low, mid)
    _merge_sort(arr, mid, high)
    _merge_arr(arr, low, mid, high)


def _merge_arr(arr: List, low: int, mid: int, high: int):
    """
    合并两个数组
    :param arr:待合并数组
    :param low: 第一个序列最小索引
    :param mid: 第二个序列最小索引，
    :param high: 第二个序列最大索引+1
    :return:
    """
    i = low
    j = mid
    sorted_list = []
    while i < mid and j < high:
        if arr[i] <= arr[j]:
            sorted_list.append(arr[i])
            i += 1
        else:
            sorted_list.append(arr[j])
            j += 1

    if i == mid:
        sorted_list.extend(arr[j:high])
    else:
        sorted_list.extend(arr[i:mid])
    arr[low:high] = sorted_list


if __name__ == '__main__':
    my_arr = [4, 6, 2, 8, 9]
    print(merge_sort(my_arr))