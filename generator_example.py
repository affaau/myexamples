import random


def bernoulli_process(p):
    if p > 1.0 or p < 0.0:
        raise ValueError("p should be between 0.0 and 1.0.")

    while True:
        yield random.random() < p


def von_neumann_extractor(process):
    while True:
        x, y = process.next(), process.next()
        if x != y:
            yield x


def count_generator():
    n = 0
    while True:
        yield n
        n += 1


def hofstadter_generator(s):
    a = s[:]
    while True:
        try:
            q = a[-a[-1]] + a[-a[-2]]
            a.append(q)
            yield q
        except IndexError:
            return


def tent_map(mu, x0):
    x = x0
    while True:
        yield x
        x = mu * min(x, 1.0 - x)


def collatz(n):
    yield n
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        yield n


if __name__ == '__main__':
    counter = count_generator()
    print(counter)
    print(next(counter))
    print(next(counter))

    print(iter(counter))
    print(iter(counter) is counter)
    print(type(counter))

    h = hofstadter_generator([1, 1])
    for __ in range(10):
        print(next(h), end=", ")
    print()

    t = tent_map(2.0, 0.1)
    for __ in range(30):
        print("%.1f" % (next(t),))

    print(list(collatz(7)))
    print(list(collatz(13)))
