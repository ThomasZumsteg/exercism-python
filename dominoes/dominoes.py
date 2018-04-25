def chain(dominoes):
    if len(dominoes) == 0:
        return []
    queue = [((dominoes[0],), tuple(dominoes[1:]))]
    while queue:
        chain, pool = queue.pop()
        tail = chain[-1][-1] 
        if chain[0][0] == tail and len(pool) == 0:
            return chain
        for d, domino in enumerate(pool):
            if domino[0] != tail:
                domino = (domino[1], domino[0])
            if domino[0] == tail:
                queue.append((chain + (domino,), pool[:d] + pool[d+1:]))
