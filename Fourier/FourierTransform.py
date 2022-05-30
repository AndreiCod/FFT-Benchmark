import Fourier
import numpy as np


def fft(x: np.ndarray) -> np.ndarray:
    """
       A recursive implementation of
       the 1D Cooley-Tukey FFT, the
       input should have a length of
       power of 2.
    """
    n = len(x)

    if n == 1:
        return x

    x_even = fft(x[::2])
    x_odd = fft(x[1::2])
    factor = np.exp(2j * np.pi * np.arange(n) / n)
    x_fft = np.concatenate([x_even + factor[:int(n / 2)] * x_odd, x_even + factor[int(n / 2):] * x_odd])

    return x_fft


def __ifft(x: np.ndarray) -> np.ndarray:
    """
           A recursive implementation of
           the 1D Cooley-Tukey IFFT, the
           input should have a length of
           power of 2.
        """
    n = len(x)

    if n == 1:
        return x

    x_even = __ifft(x[::2])
    x_odd = __ifft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(n) / n)
    x_ifft = np.concatenate([x_even + factor[:int(n / 2)] * x_odd, x_even + factor[int(n / 2):] * x_odd])

    return x_ifft


def ifft(x: np.ndarray) -> np.ndarray:
    return __ifft(x) / len(x)
