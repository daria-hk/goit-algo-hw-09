import timeit
arr_of_coins = [50, 25, 10, 5, 2, 1]

def find(sum):
    result = {}  
    #для вазначання монет використаного номіналу
    for coins in arr_of_coins:
        count = 0
        while sum >= coins:
            sum -= coins
            count += 1
            #print(f"Take: {coins}, left: {sum}")
        if count > 0:
            result[coins] = count
    return result

#sum = 113
sum = 15555513
result = find(sum)
print(f"Coins used to reach {sum}: {result}")

execution_time_find = timeit.timeit(lambda: result, number=10000)
print(f"Execution time of find function: {execution_time_find} seconds")

