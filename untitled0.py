# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:09:11 2019

@author: Suraj
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

frequency_sampling, audio_signal = wavfile.read("D:\\Speech\\male.wav")

print('\nSignal shape:', audio_signal.shape)
print('Signal Datatype:', audio_signal.dtype)
print('Signal duration:', round(audio_signal.shape[0] / 
float(frequency_sampling), 2), 'seconds')

audio_signal = audio_signal / np.power(2, 15)

audio_signal = audio_signal [:100]
time_axis = 1000 * np.arange(0, len(audio_signal), 1) / float(frequency_sampling)

plt.plot(time_axis, audio_signal, color='blue')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Amplitude')
plt.title('Input audio signal')
plt.show()



length_signal = len(audio_signal)
half_length = np.ceil((length_signal + 1) / 2.0).astype(np.int)

signal_frequency = np.fft.fft(audio_signal)

signal_frequency = abs(signal_frequency[0:half_length]) / length_signal
signal_frequency **= 2

len_fts = len(signal_frequency)

if length_signal % 2:
   signal_frequency[1:len_fts] *= 2
else:
   signal_frequency[1:len_fts-1] *= 2
   
signal_power = 10 * np.log10(signal_frequency)

x_axis = np.arange(0, half_length, 1) * (frequency_sampling / length_signal) / 1000.0

plt.figure()
plt.plot(x_axis, signal_power, color='black')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Signal power (dB)')
plt.show()

