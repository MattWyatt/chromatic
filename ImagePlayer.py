from PIL import Image
import numpy as np
import Player


class ImagePlayer:
    def __init__(self, path):
        self.image = Image.open(path).convert("RGB").resize((16, 16))
        self.pixels = np.asarray(self.image).reshape(self.image.width * self.image.height, 3)

    def play(self):
        p = Player.Player(3)
        for pixel in self.pixels:
            p.play_color(pixel)
