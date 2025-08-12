python3 -c "
import multiprocessing
def stress(): 
    while True: [x**2 for x in range(1000)]
procs = [multiprocessing.Process(target=stress) for _ in range(multiprocessing.cpu_count())]
[p.start() for p in procs]
"
