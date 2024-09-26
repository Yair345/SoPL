def isPalindrome(n):
    s = str(n)
    def TisPalindrome(s, h, t):
        if h == t:
            return True
        elif t - h == 1:
            return s[h] == s[t]
        return s[h] == s[t] and TisPalindrome(s, h + 1, t - 1)
    return TisPalindrome(s, 0, len(s)-1)


print(isPalindrome(123454321))