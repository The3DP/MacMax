python3 -c "
import multiprocessing
def extreme():
    data = []
    while True:
        data.append([x**2 for x in range(10000)])
procs = [multiprocessing.Process(target=extreme) for _ in range(multiprocessing.cpu_count())]
[p.start() for p in procs]
"
