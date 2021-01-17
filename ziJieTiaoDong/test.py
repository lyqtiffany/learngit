strA = "abcaaabbbdsdgba"
subStr = "ab"



while subStr in strA:
    strA = strA.replace(subStr, "", len(strA))
print(strA)



