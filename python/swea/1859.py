tot = int(input())
def getProfit(costs, std):
  return std * len(costs) - sum(costs)

for i in range(tot):
  _ = int(input())
  ans = 0
  costs = list(map(int, input().split()))
  if costs.index(max(costs)) == 0 :
    ans = 0
    continue
  while costs:
    ans += getProfit(costs[:costs.index(max(costs))], costs[costs.index(max(costs))])
    try:
        costs = costs[costs.index(max(costs))+1:]
    except:
        break
  print("#"+str(i+1),ans)