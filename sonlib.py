import pygame


def sonbut():
    pygame.init()
    pygame.mixer.music.load("butcanal.wav")
    pygame.mixer.music.play()


if __name__ == "__main__":
    sonbut()
