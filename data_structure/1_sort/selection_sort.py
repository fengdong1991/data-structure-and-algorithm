"""
选择排序
平均时间复杂度：O(n²)
最好情况: O(n²)
最坏情况: O(n²)
空间复杂度: O(1)
稳定性： 不稳定
排序方式：比较排序
排序逻辑：找到数组里最小的元素和第一个值交换，然后再从剩余的找最小值和第二个交换，直到遍历完
        数组
"""
from typing import List


def selection_sort(lists: List):
    list_len = len(lists)

    for i in range(list_len):
        min_index = i
        for j in range(i + 1, list_len):
            if lists[j] < lists[min_index]:
                min_index = j
        if min_index != i:
            lists[min_index], lists[i] = lists[i], lists[min_index]
    return lists


if __name__ == '__main__':
    my_arr = [4, 6, 2, 8, 9]
    print(selection_sort(my_arr))