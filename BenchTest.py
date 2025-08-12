import time
import multiprocessing

# Single-thread benchmark
def single_thread_test():
    start = time.time()
    total = 0
    for i in range(100_000_000):
        total += i * i
    end = time.time()
    print(f"Single-thread CPU test time: {end - start:.2f} seconds")

# Multi-thread benchmark
def worker():
    total = 0
    for i in range(25_000_000):
        total += i * i

def multi_thread_test():
    cpu_cores = multiprocessing.cpu_count()
    print(f"Running on {cpu_cores} CPU cores...")
    start = time.time()
    procs = [multiprocessing.Process(target=worker) for _ in range(cpu_cores)]
    [p.start() for p in procs]
    [p.join() for p in procs]
    end = time.time()
    print(f"Multi-thread CPU test time: {end - start:.2f} seconds")

if __name__ == "__main__":
    print("🔍 Starting CPU benchmark...\n")
    single_thread_test()
    print()
    multi_thread_test()
