from sys import argv
import pygame
import Player
import ImagePlayer
import Visualizer


if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 1, 1024)
    pygame.init()

    v = Visualizer.Visualizer(640, 480)
    p = Player.Player(3, v)
    i = ImagePlayer.ImagePlayer(argv[1], p)
    v.start()
    i.play()
