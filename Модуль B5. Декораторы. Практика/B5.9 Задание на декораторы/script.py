import time

def time_this(num_runs=10):
    time_lists = []
    def func_wrap(fun):
        def f():
            for _ in range(num_runs):
                start = time.time()
                fun()
                time_lists.append(time.time()-start)
            return sum(time_lists)/len(time_lists)
        return f
    return func_wrap


@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass

print(f())
