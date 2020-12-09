str = 'abaaacasddddfdf'
def countCharTime(str, n):
    for s in str:
        if str.count(s) == n:
            return s
        # break
    # return s

print(countCharTime('aaabbbccdwef', 2))