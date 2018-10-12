from sys import argv
import pygame
import ImagePlayer


if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 1, 1024)
    pygame.init()

    i = ImagePlayer.ImagePlayer(argv[1])
    i.play()