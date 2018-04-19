def measure(bucket_one, bucket_two, goal, start_bucket):
    seen = set()
    if start_bucket == 'one':
        seen.add((0, bucket_two))
        vol_one, vol_two = bucket_one, 0
    elif start_bucket == 'two':
        seen.add((bucket_one, 0))
        vol_one, vol_two = 0, bucket_two
    else:
        raise ValueError('Only two buckets: {}'.format(start_bucket))

    queue = [(1, vol_one, vol_two)]

    while queue:
        steps, one, two = queue.pop(0)
        if (one, two) in seen:
            continue
        seen.add((one, two))

        if one == goal:
            return (steps, "one", two)
        elif two == goal:
            return (steps, "two", one)

        # Fill
        queue.append((steps + 1, one, bucket_two))
        queue.append((steps + 1, bucket_one, two))

        # Empty
        queue.append((steps + 1, one, 0))
        queue.append((steps + 1, 0, two))

        # Transfer
        if one + two < bucket_two:
            queue.append((steps + 1, 0, one+two))
        else:
            queue.append((steps + 1, one+two-bucket_two, bucket_two))

        if one + two < bucket_one:
            queue.append((steps + 1, one+two, 0))
        else:
            queue.append((steps + 1, bucket_one, one+two-bucket_one))

    raise ValueError('No solution')
