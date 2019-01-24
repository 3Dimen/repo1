class Fib:
    def __init__(self, max = None):
        self.previous = 0
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.previous, self.current  = Self.Current, Self.Previous + self.current
        return self.previous
class
def fibGenerator(numTerms):
    first = 0
    second = 1
    for i in range(numTerms):
        yield first
        first,second = second, first + second


def foo(x): return x
