def isBadVersion(num):
    if type(num) == int:
        return False
    if type(num) == str:
        return True
def findBadVersion(arr):
    n = len(arr)
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(arr[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return left

testArr = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
print(findBadVersion(testArr))

