from PIL import Image
import numpy as np
import Player


class ImagePlayer:
    def __init__(self, path, player=None):
        self.image = Image.open(path).convert("RGB").resize((16, 16))
        self.pixels = np.asarray(self.image).reshape(self.image.width * self.image.height, 3)
        self.player = player
        if not self.player:
            self.player = Player.Player(3)

    def play(self):
        for pixel in self.pixels:
            self.player.play_color(pixel)
