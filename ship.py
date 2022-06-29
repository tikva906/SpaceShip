import pygame
class Ship:
    # клас корабля
    def __init__(self, screen):
        # объявить и инициализировать экран, который мы приняли
        self.Screen = screen
        # Получить сетку (координатную) экрана
        self.ScreenRect = self.Screen.get_rect()
        # Загрузить картинку корабля
        self.image = pygame.image.load("Images/ship.png")
        # Получить сетку этой картинки
        self.rect = self.image.get_rect()
        # Отпозиционировать сетку картинки на сетке экрана
        self.rect.midbottom = self.ScreenRect.midbottom
        self.isRight = False
        self.isLeft = False
    def Blitme(self):
        self.Screen.blit(self.image,self.rect)

    def update(self):
        if self.isRight == True:
            self.rect.x += 1
        if self.isLeft == True:
            self.rect.x -= 1
