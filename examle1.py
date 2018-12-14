class DoubleRepr(object):
    def __str__(self):
        return "Hi, I'm a __str__"

    def __repr__(self):
        return "Hi, I'm a __repr__"

dr = DoubleRepr()
print(dr)

import os

temp_dir = '/tmp/'
filename = os.path.join(temp_dir, 'large_re_file.txt')
try:
    infile = open(filename, 'r')
except:
    print('filename {} not found'.format(filename))



print(filename)