import pygame
import sys
from settings import Settings
from ship import Ship

class SpaceShip:
    def __init__(self):
        # Инициализация движка для того, чтобы мы могли с ним работать
        pygame.init()
        # Созждаем объект настроек
        self.settings = Settings()
        # Получение объекта экрана с установленным разрешением 1200 на 800 пикселей (ширина и высота)
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        pygame.display.set_caption('Plate')
        # создаем объект иконки
        icon = pygame.image.load('logo.ico')
        # Устанавливаем иконку
        pygame.display.set_icon(icon)
        # Создаем объект корабля
        self.ship = Ship(self.screen)

    def Start(self):
        while True:
            # Отслеживаем события клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Задаем цвет фона
            self.screen.fill(self.settings.colour)
            # Отрисовать корабль
            self.ship.Blitme()
            # Обновление экрана (fps)
            pygame.display.flip()


if __name__ == '__main__':
    game = SpaceShip()
    game.Start()

# Пули (лазер)
# Кнопка ИГРАТЬ
# ЖИЗНИ