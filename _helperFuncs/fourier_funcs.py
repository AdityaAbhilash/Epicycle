import numpy as np

# def inv(points_fft, N):
#     #inverse fourier array
#     generated_function = np.asarray([0j for i in range(N)])

#     for tau in range(N):
#         for k in range(len(points_fft)):
#             # inverse fourier transform
#             generated_function[tau] += points_fft[k]*(np.e**(1j*2*np.pi*k*tau/N))

#     return np.divide(generated_function, N)


def inv(points_fft, N):
    generated_function = np.zeros(N, dtype=np.complex128)  # Initialize as complex array

    for tau in range(N):
        for k in range(len(points_fft)):
            # Inverse Fourier Transform calculation
            generated_function[tau] += points_fft[k] * np.exp(1j * 2 * np.pi * k * tau / N)

    return np.divide(generated_function, N)  # Normalize