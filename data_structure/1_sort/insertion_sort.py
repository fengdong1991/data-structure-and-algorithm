"""
插入排序
平均时间复杂度：O(n²)
最好情况: O(n)
最坏情况: O(n²)
空间复杂度: O(1)
稳定性： 稳定
排序方式：比较排序
排序逻辑：从第二个元素开始，把第一个元素当作已经排序好的数组，
        从后往前比较，如果小于比较的元素，则比较的元素右移一位。否则将元素放到空处。
        继续第三个元素。把元素左边的数组当作排序好的，右边表示待排序的。直到遍历完所有元素。
        则全部都是已排序好的数组。
"""
from typing import List


def insertion_sort(lists: List):
    """
    插入排序
    :param lists: 待排序数组
    :return: 已排序数组
    """
    list_len = len(lists)
    for i in range(1, list_len):
        tmp = lists[i]
        j = i - 1
        while j >= 0 and lists[j] > tmp:
            lists[j + 1] = lists[j]
            j -= 1
        lists[j + 1] = tmp
    return lists


if __name__ == '__main__':
    my_arr = [4, 6, 2, 8, 9]
    print(insertion_sort(my_arr))
