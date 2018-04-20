import re


def parse_markdown(markdown):
    res = []
    for line in markdown.split('\n'):
        line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
        line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)

        header_match = re.match(r'(#+) (.*)', line)
        if header_match:
            res.append('<h{0}>{1}</h{0}>'.format(
                len(header_match.group(1)), header_match.group(2)))
        elif line.startswith('* '):
            if res and res[-1] == '</ul>':
                res.pop()
            else:
                res.append('<ul>')
            res.append('<li>' + line[2:] + '</li>')
            res.append('</ul>')
        else:
            res.append('<p>' + line + '</p>')
    return ''.join(res)
