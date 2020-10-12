

if __name__ == "__main__":

    def gen():
        for i in range(10):
            yield i

    num_gen = gen()

    try:
        for i in range(20):
            print(next(num_gen))
    except StopIteration:
        print("I don't have nay more")


    def lazy_gen():
        i = 0
        while True:
            yield i
            i += 5

    lazy = lazy_gen()
    for i in range(20):
        print(next(lazy))
