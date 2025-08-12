python3 -c "
import multiprocessing
def burn(n): [x**2 for x in range(10**6)]
procs = [multiprocessing.Process(target=burn, args=(i,)) for i in range(multiprocessing.cpu_count())]
[p.start() for p in procs]
[p.join() for p in procs]
"
