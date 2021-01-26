import pygame
# inicializando o mixer Pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('04-Sinônimos.mp3')
pygame.mixer.music.play()
pygame.event.wait()
