def coinSum(coins, sum):
    # Stop condition.
    if sum == 0:
        return [[]]

    # Recursive step
    solutions = []
    for i, coin in enumerate(coins):
        if coin <= sum:
            lst = coinSum(coins[i:], sum - coin)
            solutions.extend([[coin] + l for l in lst])
    return solutions


coins=list(map(int,input().split()))

sum=int(input())

print(coinSum(coins, sum))