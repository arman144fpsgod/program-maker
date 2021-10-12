import pygame
pygame.mixer.init()  # Initialize the mixer module.
sound1 = pygame.mixer.Sound('D:\myfiles\music\Mymusic.ogg')  # Load a sound.

while True:
    inpt = input('Press enter to play the sound: ')
    sound1.play()  # Play the sound.
    print('Playing sound')
