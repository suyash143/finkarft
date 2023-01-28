s1 = 'qwertyuiopasdfghjkl'
s2 = 'zxcvbnmsdfghjklqwerttyuiop'


def longest_substring(s1, s2):
    ans = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            k = 0
            while (i + k) < len(s1) and (j + k) < len(s2) and s1[i + k] == s2[j + k]:
                k += 1
            ans = (max(ans, k))
    return ans


print(longest_substring(s1,s2))