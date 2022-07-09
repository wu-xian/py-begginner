class Rabbit:
    iteration = 0
    payloads = []
    def __iter__(self):
        self.iteration = 0
        return self
    def __next__(self):
        res = self.payloads[self.iteration]
        self.iteration += 1
        return res
def func():
    ra = Rabbit()
    ra.payloads = [1,3,5,7]
    it = iter(ra)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

func()
    

