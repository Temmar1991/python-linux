import re
import os


def run_re():
    pattern = 'pDq'

    temp_dir = '/tmp/'
    filename = os.path.join(temp_dir, 'large_re_file.txt')
    infile=open(filename,'r')
    match_count = 0
    lines = 0
    for line in infile:
        match = re.search(pattern, line)
        if match:
            match_count += 1
            line += 1
    return (lines, match_count)


if __name__ == "main":
    lines, match_count = run_re()
    print('LINES::, {}'.format(lines))
    print('MATCHES::,{}'.format(match_count))
