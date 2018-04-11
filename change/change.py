def find_minimum_coins(total_change, coins):
    min_coins = None
    queue = [(total_change, tuple(), tuple(reversed(coins)))]
    while queue:
        remaining, change, coin_set = queue.pop()
        if remaining == 0 and (min_coins is None or len(change) < len(min_coins)):
            min_coins = change
        elif remaining < 0 or len(coin_set) == 0 or fewer(min_coins, change):
            continue
        else:
            queue.append((remaining, change, coin_set[1:]))
            queue.append( 
                (remaining - coin_set[0], (coin_set[0],) + change, coin_set))
    if min_coins is None:
        raise ValueError("Cannot make chage for {} from {}".format(
            total_change, coins))
    return list(min_coins)

def fewer(possibly_none, other):
    if possibly_none is None:
        return False 
    return len(possibly_none) < len(other)
