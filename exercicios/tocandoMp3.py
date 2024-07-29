import pygame
import time

pygame.init()
pygame.mixer.music.load('tocandoMp3.mp3')
pygame.mixer.music.play()

# Era por conta disso que não funcionava, estava faltando essa parte

# Obtenha o comprimento da música em segundos
tamanhoMusica = pygame.mixer.Sound('tocandoMp3.mp3').get_length()

# Aguarde até a música terminar
time.sleep(tamanhoMusica)
 
pygame.event.wait()