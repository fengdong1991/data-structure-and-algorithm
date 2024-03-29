"""
计数排序
平均时间复杂度：O(n+k)  k等于数组元素可能取值
最好情况: O(n+k)
最坏情况: O(n+k)
空间复杂度: O(k)
稳定性： 稳定
排序方式：非比较排序
排序逻辑：1.建立临时数组，数组大小为数组元素可能取值。
        2.遍历元素，把元素放到临时数组里，计数+1
        3.遍历临时数组，存入数据。
"""
from typing import List


def count_sort(arr: List):
    """
    计数排序
    :param arr: 待排序数组
    :return: 已排序数组
    """
