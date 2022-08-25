def coinSum(coins, sum):
    if sum == 0:
        return [[]]
    solutions = []
    for i, coin in enumerate(coins):
        if coin <= sum:
            lst = coinSum(coins[i:], sum - coin)
            solutions.extend([[coin] + l for l in lst])
    return solutions
coins=list(map(int,input().split()))
sum=int(input())
coinSum(coins, sum)
l=coinSum(coins, sum)
l.sort(key=len)
print(l[0])
