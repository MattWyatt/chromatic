from threading import Thread
import pygame
import numpy as np


class Visualizer:
    def __init__(self, width, height):
        self.notes = []

        self.running = False

        self.width = width
        self.height = height

        pygame.display.set_caption("Visualizer")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(pygame.Color(0, 0, 0, 0))

    def update(self, notes):
        print(self.notes)
        self.notes = notes

    def start(self):
        self.running = True

        def draw_wave(frequency, color):
            plot_points = [[0, 0]]
            for x in range(0, self.width):
                y = int(np.sin(x / self.width * frequency * np.pi) * 200 + 240)
                plot_points.append([x, y])
            pygame.draw.lines(self.screen, color, False, plot_points, 2)
            pygame.display.flip()
            self.screen.fill(pygame.Color(0, 0, 0, 0))

        def loop():
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                for note in self.notes:
                    draw_wave(note.frequency, note.color)

        Thread(target=loop, daemon=True).start()
