from collections import defaultdict

def poker(hands):
    """poker determines the best poker hand from a set of hands"""
    best_hands, best_score = [], None
    for hand in hands:
        score = score_hand(hand)
        if best_score == None or best_score < score:
            best_hands, best_score = [hand], score
        elif best_score == score:
            best_hands.append(hand)
    return best_hands

def score_hand(hand):
    """score_hand scores a poker hand based on it's type and the cards"""
    suits, ranks = get_suits_and_ranks(hand)
    sorted_ranks = sorted(ranks.keys())
    kinds = sorted(list(ranks.values()), reverse=True)

    flush = all(suit == suits[0] for suit in suits)
    straight = all(sorted_ranks[0] + i == rank for i, rank in enumerate(sorted_ranks))

    if sorted_ranks == [2,3,4,5,14]:
        straight, ranks = True, {1:1, 2:1, 3:1, 4:1, 5:1}

    if flush and straight:
        score = 8
    elif kinds == [4,1]:
        score = 7
    elif kinds == [3,2]:
        score = 6
    elif flush:
        score = 5
    elif straight:
        score = 4
    elif kinds == [3,1,1]:
        score = 3
    elif kinds == [2,2,1]:
        score = 2
    elif kinds == [2,1,1,1]:
        score = 1
    else:
        score = 0

    hand = sorted(ranks.items(), key=lambda r: (-r[1], -r[0]))
    return [score] + [v for v,c in hand for _ in range(c)]

def get_suits_and_ranks(hand):
    """get_suits_and_ranks splits a hand into suits and ranks"""
    suits, ranks = [], defaultdict(int)
    for card in hand:
        suit, rank = card[-1], card[:-1]
        suits.append(suit)
        ranks[ convert_rank(rank) ] += 1
    return suits, ranks

"""convert_rank converts a rank to an integer"""
convert_rank = lambda c: '--23456789TJQKA'.index(c)


