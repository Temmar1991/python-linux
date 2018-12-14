import re
<<<<<<< HEAD
import os

=======
<<<<<<< HEAD
import os

=======
>>>>>>> 222f6009832b976bb9d9a93603fe623dd4a787d9
>>>>>>> f1e02f7fff9a598cb5d74c2ef3dba691ef1985af

def run_re():
    pattern = 'pDq'

<<<<<<< HEAD
    temp_dir = '/tmp/'
    filename = os.path.join(temp_dir, 'large_re_file.txt')
    infile=open(filename,'r')
=======
<<<<<<< HEAD
    temp_dir = '/tmp/'
    filename = os.path.join(temp_dir, 'large_re_file.txt')
    infile=open(filename,'r')
=======
    infile=open('large_re_file.txt','r')
>>>>>>> 222f6009832b976bb9d9a93603fe623dd4a787d9
>>>>>>> f1e02f7fff9a598cb5d74c2ef3dba691ef1985af
    match_count = 0
    lines = 0
    for line in infile:
        match = re.search(pattern, line)
        if match:
            match_count += 1
            line += 1
    return (lines, match_count)

<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
>>>>>>> 222f6009832b976bb9d9a93603fe623dd4a787d9
>>>>>>> f1e02f7fff9a598cb5d74c2ef3dba691ef1985af
if __name__ == "main":
    lines, match_count = run_re()
    print('LINES::, {}'.format(lines))
    print('MATCHES::,{}'.format(match_count))
