#Python-同时寻找出数组中的最大值和最小值
def find_max_min(*lst):
    if not lst:
        print('list is empty')
        return None
    max_value, min_value = lst[0], lst[0]
    for item in lst:
        if not isinstance(item, int):
            print('item should be int')
            return None
        if item > max_value:
            max_value = item
        if item < min_value:
            min_value = item
    print('最大值{0},最小值{1}'.format(max_value, min_value))
if __name__ == '__main__':
    find_max_min(1, 2, 1)
    find_max_min(1, 2, 'b')
    find_max_min('a', 'b')
    find_max_min()