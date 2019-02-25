import time

def loop(N):
    start = time.time()
    numbers = range(N)
    size = len(numbers)
    evens = []
    i = 0
    while i < size:
        if i % 2 == 0:
            evens.append(i)
        i += 1
    print(time.time()-start) 

def comprehensive(N):
    start = time.time()
    evens = [i for i in range(N) if i % 2 == 0]
    print(time.time()-start)

def gen_dict(N):
    start = time.time()
    i = 0
    seq = ["one", "two", "three"]*N
    for element in seq:
        seq[i] = '%d: %s' % (i, seq[i])
        i += 1
    print(time.time()-start)

def _treatment(pos, element):
    return '%d: %s' % (pos, element)

def speed_enumurate(N):
    start = time.time()
    seq = ["one", "two", "three"]*N
    #seq = [_treatment(i, el) for i, el in enumerate(seq)]
    for i, element in enumerate(seq):
        seq[i] = '%d: %s' % (i, seq[i])
    print(time.time()-start)

if __name__ == '__main__':
    loop(100000)               # 0.019963 sec
    comprehensive(100000)      # 0.010028 sec (double the speed and neat)

    gen_dict(10000)            # 0.010024 sec
    speed_enumurate(10000)     # 0.010024 sec (same speed but neat)
