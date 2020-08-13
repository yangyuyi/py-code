class Lst:
    def __init__(self, start):
        self._start = start

    def _advance(self):
        self._start += 1

    def __next__(self):
        if self._start is None:
            raise StopIteration()
        else:
            a = self._start
            self._advance()
            return a

    def __iter__(self):
        return self

    def run(self, num):
        for j in range(num):
            print(self.__next__(), end=' ')
        print()


class AP(Lst):
    def __init__(self, start, increment):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._start += self._increment


class GP(Lst):
    def __init__(self, start, base):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._start *= self._base


class Fib(Lst):
    def __init__(self, first, second):
        super().__init__(first)
        self._diff = second - first

    def _advance(self):
        temp = self._diff
        self._diff = self._start
        self._start += temp


if __name__ == '__main__':
    print('从1开始共10个数基础数列：')
    Lst(1).run(10)

    print('从2开始公差为5数量为10的等差数列:')
    AP(2, 5).run(10)

    print('从2开始公比为3项数为10的等比数列:')
    GP(2, 3).run(10)

    print('起始值为4和6的fibonacci数列:')
    Fib(4, 6).run(10)
