

if __name__ == "__main__":

    names = ['samer', 'bashar', 'aziz', 'majd', 'basma']
    def gen():
        for name in names:
            yield name

    names_gen = gen()

    try:
        for i in range(20):
            print(next(names_gen))
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
