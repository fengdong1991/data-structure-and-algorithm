"""
冒泡排序
平均时间复杂度：O(n²)
最好情况: O(n)
最坏情况: O(n²)
空间复杂度: O(1)
稳定性： 稳定
排序方式：比较排序
排序逻辑：遍历数组，每次比较相邻的两个元素，如果左边大于右边，则交换两者顺序，
        直到把最大元素换到最右边。
        然后再遍历数组前面n-1个元素。相同的方法把第二大元素换到最右边。
        依次循环遍历。直到某一个遍历未出现元素交换，则停止循环。
        此时就是排序好的数组。
"""
from typing import List


def bubble_sort(lists: List):
    """
    冒泡排序
    :param lists: 待排序数组
    :return: 排序好数组
    """
    # 获取数组长度
    list_len = len(lists)

    for i in range(list_len):
        switch_flag = False
        for j in range(list_len - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
                switch_flag = True
        if not switch_flag:
            break
    return lists


if __name__ == '__main__':
    my_arr = [4, 6, 2, 8, 9]
    print(bubble_sort(my_arr))
