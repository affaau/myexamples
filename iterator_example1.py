# for python 2
class qsequence(object):
    def __init__(self, s):
        self.s = s[:]

    def next(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.s


# for python 3
class qsequence3(object):
    def __init__(self, s):
        self.s = s[:]

    def __next__(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.s


if __name__ == '__main__':
    import sys
    # check python version
    flag = 3 if sys.version_info > (3, 0) else 2
    # define functions accordingly
    Range = range if flag == 3 else xrange
    Q = qsequence3([1, 1]) if flag == 3 else qsequence([1, 1])

    print(next(Q))
    print(next(Q))
    print([next(Q) for __ in Range(10)])
