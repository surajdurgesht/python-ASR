# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:52:47 2019

@author: Suraj
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

output_file = 'D:\\Speech\\male.wav'

duration = 4 # in seconds
frequency_sampling = 44100 # in Hz
frequency_tone = 784
min_val = -4 * np.pi
max_val = 4 * np.pi

t = np.linspace(min_val, max_val, duration * frequency_sampling)
audio_signal = np.sin(2 * np.pi * frequency_tone * t)

write(output_file, frequency_sampling, signal_scaled)

audio_signal = audio_signal[:100]
time_axis = 1000 * np.arange(0, len(audio_signal), 1) / float(frequency_sampling)

plt.plot(time_axis, audio_signal, color='blue')
plt.xlabel('Time in milliseconds')
plt.ylabel('Amplitude')
plt.title('Generated audio signal')
plt.show()