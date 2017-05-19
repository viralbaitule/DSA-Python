def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    n=len(haystack)
    m=len(needle)
    if not (n and m):
        return 0
    for i in range(n-m+1):
        print (haystack[i:i+m])
        if haystack[i:i+n]==needle:
            print (haystack)
            return i
    return -1

print(strStr("bapple",'app'))

