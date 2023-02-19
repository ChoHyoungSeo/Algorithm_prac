def isPalindrome(s, start, end, ans):
  if start >= end:
    return (1, ans+1)
  elif s[start] != s[end]:
    return (0, ans+1)
  else:
    return isPalindrome(s, start + 1, end - 1, ans+1)

if __name__ == "__main__":
  tot = int(input())
  for _ in range(tot):
    s = input()
    (result, ans) = isPalindrome(s, 0, len(s)-1, 0)
    print(result, ans)