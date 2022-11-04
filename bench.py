from time import perf_counter


class BenchData:
    def __init__(self):
        self._names = []
        self._runtimes = []

    def add(self, name, runtime):
        self._names.append(name)
        self._runtimes.append(runtime)

    def __repr__(self):
        msg = ""
        for n, t in zip(self._names, self._runtimes):
            msg += f"{n}: {t} ms\n"
        return msg


# A decorator to benchmark exercises
def benchmark(exercise_name, bench_data=None):
    def wrap(f):
        def wrapped_f(*args):
            print(f"\n----- {exercise_name} -----")
            t1 = perf_counter()
            f(*args)
            if bench_data:
                tdelta = round((perf_counter() - t1) * 1000, 3)
                bench_data.add(exercise_name, tdelta)

        return wrapped_f

    return wrap
