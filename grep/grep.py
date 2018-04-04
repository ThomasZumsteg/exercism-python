def grep(pattern, files, flags=''):
    matches = []
    for file_name in files:
        file_matches = []
        for l, line in enumerate(open(file_name).readlines(), 1):
            if match(pattern, line, flags):
                file_matches.append((l, line))
                if 'l' in flags:
                    break
        matches.append((file_name, file_matches))
    return formatter(matches, flags)

def match(pattern, line, flags):
    if 'i' in flags:
        pattern, line = pattern.lower(), line.lower()

    if 'x' in flags:
        return pattern == line.strip()
    elif 'v' in flags:
        return pattern not in line

    return pattern in line

def formatter(matches, flags):
    output = []

    if 'l' in flags:
        format_str = '{filename}\n'
    elif 'n' in flags:
        format_str = '{ln}:{line}'
    else:
        format_str = '{line}'

    if len(matches) > 1 and 'l' not in flags:
        format_str = '{filename}:' + format_str

    for filename, lines in matches:
        for ln, line in lines:
            output.append(format_str.format(ln=ln, line=line, filename=filename))
            if 'l' in flags:
                break

    return ''.join(output)
