MATCHING_BRACKETS = dict(( "()","{}","[]" ))

def check_brackets(line):
    """check_brackets checks if brackets are properly balanced"""
    queue = []
    for char in line:
        if char in MATCHING_BRACKETS:
            queue.append(MATCHING_BRACKETS[char])
        elif char in MATCHING_BRACKETS.values():
            if len(queue) <= 0 or char != queue[-1]:
                return False
            queue.pop()
    return queue == []
