import numpy as np
import multiprocessing as mp
import timeit
from Fourier.FourierTransform import fft


def array_generator(count: int, size_order: int, max_val: int = 100) -> np.ndarray:
    np.random.seed(42)
    for _ in range(count):
        yield np.random.randint(max_val, size=2 ** size_order)


def run_fft(array_count: int, array_size: int, cpu_count: int):
    if cpu_count > mp.cpu_count():
        raise Exception(f"This cpu has {mp.cpu_count()} cores, not {cpu_count}")

    pool = mp.Pool(cpu_count)
    pool.map(fft, array_generator(array_count, array_size))
    pool.close()


def fft_benchmark(passes_count: int, array_count: int, array_size: int, cpu_count: int = mp.cpu_count()):
    times = timeit.repeat(lambda: run_fft(array_count, array_size, cpu_count), number=1, repeat=passes_count)
    return times
