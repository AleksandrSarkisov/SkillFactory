import time

class Timer():
    def __init__(self, num_runs, fun):
        self.num_runs = num_runs
        self.fun = fun

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args, **kwargs):
        runtime = time.time()-self.start
        avg = runtime/self.num_runs
        print("Averge runtime of function {} for {} times is {} sec".format(self.fun.__name__, self.num_runs, avg))



def f():
    for j in range(1000000):
        pass

if __name__ == "__main__":
    with Timer(10, f):
        for _ in range(1000000):
            pass
