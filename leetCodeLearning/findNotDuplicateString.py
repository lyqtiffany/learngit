# str = 'abcabcbb', 找出字符串中不重复的最长字符串，并输出长度，此时是abc, 长度为3.

str = 'abcabcbbhijk'
'''list =[]
for item in str:
    for i in range(len(str)):
        if item == str[i] and str.index(item) != i:
            break
        else:
            list.append(str[i])
    break
print(list)
print(len(list))'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        tail = 0
        if len(s) < 2: return len(s)  # 边界条件
        res = 1
        
        while tail < len(s) - 1:
            tail += 1
            if s[tail] not in s[head: tail]:
                res = max(tail - head + 1, res)
            else:
                while s[tail] in s[head: tail]:
                    head += 1
        return res,s[head: tail]
aa = Solution()
print(aa.lengthOfLongestSubstring(str))

