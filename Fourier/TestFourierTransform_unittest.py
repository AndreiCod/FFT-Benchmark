import unittest
from Fourier.FourierTransform import fft, ifft
import numpy as np


class TestFourierTransform(unittest.TestCase):
    def test_fft_ifft(self):
        x_test = np.array([5, 3, 2, 1])
        fft_result = fft(x_test)
        ifft_result = ifft(fft_result)
        self.assertTrue(np.all(np.abs(x_test - ifft_result) < 0.00000001))


if __name__ == '__main__':
    unittest.main()
