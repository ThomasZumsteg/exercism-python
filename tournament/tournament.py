from collections import defaultdict

WIN, LOSS, DRAW = 'WIN', 'LOSS', 'DRAW'

def tally(tournament_results):
    results = defaultdict(lambda: {WIN: 0, LOSS: 0, DRAW: 0})
    for line in tournament_results.splitlines():
        home, away, result = line.split(';')
        if result == 'win':
            results[home][WIN] += 1
            results[away][LOSS] += 1
        elif result == 'loss':
            results[home][LOSS] += 1
            results[away][WIN] += 1
        elif result == 'draw':
            results[home][DRAW] += 1
            results[away][DRAW] += 1
    lines = ['{:30s} | MP |  W |  D |  L |  P'.format('Team')]
    for team in sorted(results.keys(), key=
            lambda team: (-_score(**results[team]), team)):
        lines.append('{:30s} | {:2} | {:2} | {:2} | {:2} | {:2}'.format(
            team, sum(results[team].values()),
            results[team][WIN], results[team][DRAW], results[team][LOSS],
            _score(**results[team])))
    return '\n'.join(lines)

def _score(*, WIN, LOSS, DRAW):
    return 3 * WIN + DRAW
