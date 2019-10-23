import time

class timer():
    avg_time = 0

    def __call__(self, fun):
        def time_this(num_runs=10):
            time_list = []
            def func_wrap(fun):
                def f():
                    for _ in range(num_runs):
                        start = time.time()
                        fun()
                        time_list.append(time.time()-start)
                        self.avg_time = sum(time_list)/len(time_list)
                        return self.avg_time
                return f
            return func_wrap

obj = timer()
def f():
    for j in range(1000000):
        pass

print(obj(f()))

def f1():
    l = []
    for i in range(10):
        start = time.time()
        for j in range(1000000):
            pass
        l.append(time.time()-start)
    return sum(l)/len(l)
print(f1())
