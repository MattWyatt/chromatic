import pygame
import numpy as np
import ChromaNote
import ChromaChord


class Player:
    def __init__(self, channels):
        self.num_channels = channels
        self.channels = []
        for i in range(0, self.num_channels):
            self.channels.append(pygame.mixer.Channel(i))

    def play_note(self, note):
        sound = pygame.mixer.Sound(note.samples)
        self.channels[0].queue(sound)
        for i in range(1, self.num_channels):
            self.channels[i].queue(pygame.mixer.Sound(np.zeros((note.sample_rate,)).astype(np.int16)))

    def play_chord(self, chord):
        if not chord.size <= self.num_channels:
            raise Exception

        for note, i in zip(chord.chord, range(0, self.num_channels)):
            sound = pygame.mixer.Sound(note.samples)
            self.channels[i].queue(sound)

    def play_color(self, color, volume=0.5):
        def normalize_color_value(c):
            return round(((87 * c) / 255) + 1)

        def is_chord(c):
            a = normalize_color_value(c[0])
            b = normalize_color_value(c[1])
            c = normalize_color_value(c[2])

            return abs(a - b) < 13 and abs(a - c) < 13 and abs(b - c) < 13

        if is_chord(color):
            chord = ChromaChord.ChromaChord(color[0], color[1], color[2])
            self.play_chord(chord)
            return
        note = ChromaNote.ChromaNote(color[0], color[1], color[2])
        self.play_note(note)
