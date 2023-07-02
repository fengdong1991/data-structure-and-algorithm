"""
堆排序
平均时间复杂度：O(lgn*n)
最好情况: O(lgn*n)
最坏情况: O(lgn*n)
空间复杂度: O(1)
稳定性： 不稳定
排序方式：比较排序
排序逻辑：1.建堆。 2.堆首元素和最后一个元素交换。然后剩余元素重新建堆；
        然后再和倒数第二个元素交换，剩余元素再重建，直到剩一个元素。
"""
from typing import List


def heapify(arr: List, n: int, i: int):
    """
    保证i所在节点为左右子树最大值。
    :param arr: 堆对应数组
    :param n: 堆长度
    :param i: 需要确定堆的位置的索引
    :return: 无
    """
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List):
    """
    堆排序
    :param arr: 待排序数组
    :return: 已排序好数组
    """
    arr_len = len(arr)
    # 建堆，从最后一个非叶子节点到跟元素，依次建堆置换。
    for i in range(arr_len // 2 - 1, -1, -1):
        heapify(arr, arr_len, i)

    # 每次堆首和队尾元素置换，重新建堆。
    for i in range(arr_len - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


if __name__ == '__main__':
    my_arr = [4, 6, 2, 8, 9]
    print(heap_sort(my_arr))
