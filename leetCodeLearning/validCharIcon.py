#有效的括号 20

class Solution:
    def isValid(self, s):
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if c == ')':
                        if temp != '(':
                            return False
                    elif c == ']':
                        if temp != '[':
                            return False
                    elif c == '}':
                        if temp != '{':
                            return False
        if len(stack) == 0:
            return True
        else:
            return False
if __name__ == '__main__':
    print(Solution().isValid('{}'))
