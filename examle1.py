class DoubleRepr(object):
    def __str__(self):
        return "Hi, I'm a __str__"

    def __repr__(self):
        return "Hi, I'm a __repr__"

dr = DoubleRepr()
print(dr)


