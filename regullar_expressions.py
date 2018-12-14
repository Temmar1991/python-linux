
import re
import os
import pdb


def run_re():
    pattern = 'pDq'

    temp_dir = '/tmp/'
    filename = os.path.join(temp_dir, 'large_re_file.txt')
    infile = open(filename, 'r')

    match_count = 0
    lines = 0

    pdb.set_trace()
    for line in infile:
        match = re.search(pattern, line)
        if match:
            match_count += 1
        lines += 1
    return lines, match_count


if __name__ == "__main__":
    pdb.set_trace()
    lines, match_count = run_re()
    pdb.set_trace()
    print('LINES::, {}'.format(lines))
    print('MATCHES::, {}'.format(match_count))
