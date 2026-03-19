import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sample_rate, audio = wavfile.read('apollo11.wav')
audio = audio.astype(float)


fft_coeffs = np.fft.fft(audio)
frequencies = np.fft.fftfreq(len(audio), d=1/sample_rate)

# Plot frequency spectrum to identify noise
plt.plot(np.abs(frequencies), np.abs(fft_coeffs))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.show()

# Zero out unwanted frequencies
fft_filtered = fft_coeffs.copy()
fft_filtered[(np.abs(frequencies) > 3400)] = 0   # remove high freq noise
fft_filtered[(np.abs(frequencies) < 300)] = 0    # remove low freq rumble

# Inverse FFT to get cleaned audio
cleaned_audio = np.fft.ifft(fft_filtered).real
wavfile.write('cleaned.wav', sample_rate, cleaned_audio.astype(np.int16))