import pygame
import numpy as np


class Note:
    def __init__(self, frequency, volume=0.5):
        self.frequency = frequency
        self.sample_rate = pygame.mixer.get_init()[0]
        self.volume = volume

        self.samples = np.array([4096 * np.sin(2.0 * np.pi * self.frequency * x / self.sample_rate)
                                 for x in range(0, self.sample_rate)]).astype(np.int16)
