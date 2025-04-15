import pygame
import random


class Dice:
    def __init__(self, x):
        self.x = x
        self._showingFace = 1
        self._rect = pygame.Rect(58, 88, 184, 184)

    @property
    def showingFace(self):
        return self._showingFace

    @showingFace.setter
    def showingFace(self, face):
        self._showingFace = face
        self._rect = pygame.Rect(58, 88, 184, 184)

    @property
    def rectangle(self):
        return self._rect

    def Roll(self):
        rollNumber = random.randrange(1, 7)
        self._showingFace = rollNumber
        xVal = 227 * (rollNumber - 1) + 58
        self._rect = pygame.Rect(xVal, 88, 184, 184)

    def draw(self, screen, rollDur, checked):
        if rollDur and not checked:
            rollNumber = random.randrange(6)
            xVal = 227 * (rollNumber) + 58
            rect = pygame.Rect(xVal, 88, 184, 184)
            screen.blit(pygame.image.load("images/dice.jpg"), (self.x, 20), rect)
        else:
            screen.blit(pygame.image.load("images/dice.jpg"), (self.x, 20), self._rect)

class Checkbox:
    def __init__(self, x, y, width, height, label, diceNum, checked=False):
        self.rect = pygame.Rect(x+2, y+2, width-4, height-4)
        self.outer_rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.checked = checked
        self.font = pygame.font.SysFont(None, 24)
        self.diceNum = diceNum

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.outer_rect, 2)
        if self.checked:
            pygame.draw.rect(screen, (45, 45, 45), self.rect)
        label_surface = self.font.render(self.label, True, (0, 0, 0))
        screen.blit(label_surface, (self.rect.right + 10, self.rect.top))
