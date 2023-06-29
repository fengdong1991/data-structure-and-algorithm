"""
希尔排序
平均时间复杂度：O(n*n½) 和选择的gap有关系，比O(n)大，比O(n²)小。
最好情况: O(n*n½)
最坏情况: O(n²)
空间复杂度: O(1)
稳定性： 不稳定
排序方式：比较排序
排序逻辑：把数组按某一个gap分为几组，然后每组进行插入排序。
        之后再按照gap//2分为几组，继续对每组进行插入排序，知道gap为1。插入排序结束。
"""
from typing import List


def shell_sort(arr: List):
    """
    希尔排序
    :param arr: 待排序数组
    :return: 排序号数组
    """
    arr_len = len(arr)
    gap = arr_len // 2

    while gap > 0:
        for i in range(gap, arr_len):
            tmp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > tmp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = tmp
        gap //= 2
    return arr


if __name__ == '__main__':
    my_arr = [4, 6, 2, 8, 9]
    print(shell_sort(my_arr))
