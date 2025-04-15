import pygame
import random


class Dice:
    def __init__(self, x):
        self._x = x
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
            screen.blit(pygame.image.load("images/dice.png"), (self._x, 20), rect)
        else:
            screen.blit(pygame.image.load("images/dice.png"), (self._x, 20), self._rect)

def draw_rounded_rect(surface, rect, radius, color):
    """
    Draws a rectangle with rounded corners.
    """
    rect = pygame.Rect(rect)
    border_rect = rect.inflate(-2 * radius, -2 * radius)
    pygame.draw.rect(surface, color, border_rect, border_radius=5)
    # corner_rect = pygame.Rect(rect.x, rect.y, 2 * radius, 2 * radius)
    # pygame.draw.ellipse(surface, color, corner_rect)
    # corner_rect.move_ip(rect.width - 2 * radius, 0)
    # pygame.draw.ellipse(surface, color, corner_rect)
    # corner_rect.move_ip(0, rect.height - 2 * radius)
    # pygame.draw.ellipse(surface, color, corner_rect)
    # corner_rect.move_ip(rect.width - 2 * radius, 0)
    # pygame.draw.ellipse(surface, color, corner_rect)


class Button:
    def __init__(self, x, y, width, height, text, font_size, default_color, hover_color, click_color, shadow_color,
                 callback):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.SysFont(None, font_size)
        self.default_color = default_color
        self.hover_color = hover_color
        self.click_color = click_color
        self.shadow_color = shadow_color
        self.current_color = self.default_color
        self.callback = callback  # Function to execute on click

    def draw(self, screen):
        # Render the text
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2

        # Draw the shadow with a slight offset
        shadow_offset = 2  # Adjust this value for shadow intensity
        draw_rounded_rect(screen, (self.x + shadow_offset, self.y + shadow_offset, self.width, self.height), 5,
                          self.shadow_color)

        # Draw the button with rounded corners
        draw_rounded_rect(screen, (self.x, self.y, self.width, self.height), 5, self.current_color)

        # Draw the text on the button
        screen.blit(text_surface, (text_x, text_y))

    def handle_event(self, event):
        # Check if mouse is hovering over the button
        mouse_pos = pygame.mouse.get_pos()
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            self.current_color = self.hover_color
            # Check for click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.current_color = self.click_color
                if self.callback:
                    self.callback()  # Execute callback function
        else:
            self.current_color = self.default_color

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

    def handle_event(self, event):
        keyList = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g]
        if event.type == pygame.KEYDOWN:
            if event.key == keyList[self.diceNum]:
                self.checked = not self.checked
