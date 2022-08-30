def longest_consec(strarr, k):
    result = ""
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    else:
        for i in range(n - k + 1):
            s = "".join(strarr[i: i + k])
            if len(s) > len(result):
                result = s
    return result
  
