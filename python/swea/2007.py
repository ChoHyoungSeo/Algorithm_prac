from collections import deque
tot = int(input())

def checkPattern(tmp_words, std):
  try:
    std += tmp_words.popleft()
  except:
    return ''
  while True:
    if std != ''.join(list(tmp_words)[:len(std)]) or std != ''.join(list(tmp_words)[len(std):len(std)*2]):
      try:
        tmp_words = deque(tmp_words)
        std += tmp_words.popleft()
      except:
        std = ''
        break
    else:
      break
  return std
  
for i in range(tot):
  words = input()
  tmp_words = deque(words)
  std = ''
  ans = checkPattern(tmp_words, std)
  print("#"+str(i+1), len(ans))