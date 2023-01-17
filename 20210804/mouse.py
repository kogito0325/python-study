import pygame


class Mouse:
    def __init__(self):
        self.x, self.y = 0, 0
        self.clicked = False

    def handle(self, event):
        self.x, self.y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
