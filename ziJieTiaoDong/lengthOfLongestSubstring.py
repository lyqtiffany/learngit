#最长不含重复字符的子字符串
#双指针 + 哈希表
class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res

if __name__ == '__main__':
    str = 'asdfsfds'
    test = Solution()
    print(test.lengthOfLongestSubstring(str))