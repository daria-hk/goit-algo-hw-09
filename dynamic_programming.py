import timeit
arr_of_coins = [50, 25, 10, 5, 2, 1]

def find_min_coins(sum):
    result = {}

    #ініціалізація
    min_coins = [float('inf')] * (sum + 1)
    last_coin = [-1] * (sum + 1)
    
    min_coins[0] = 0
    
    #заповнити таблицю мінімальних монет для кожної суми
    for i in range(1, sum + 1):
        for coin in arr_of_coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    #для вазначання монет використаного номіналу
    while sum > 0:
        coin = last_coin[sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        sum -= coin
       # print(f"Take: {coin}, left: {sum}")  
    return result

#sum = 113
sum = 15555513
result = find_min_coins(sum)
print(f"Coins used to reach {sum}: {result}")

execution_time_find = timeit.timeit(lambda: result, number=10000)
print(f"Execution time of find_min_coins function: {execution_time_find} seconds")
