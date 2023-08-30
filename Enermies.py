import random
import pygame
import math

class Enemy:
    def __init__(self,speed=0.5, size=20):
        self.x = random.randrange(1,500)
        self.y = random.randrange(1,500)
        self.target_x = 224
        self.target_y = 144
        self.speed = speed
        self.size = size
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)
        self.img = pygame.image.load(random.choice(['assets/pest.png','assets/pest1.png','assets/pest2.png','assets/pest3.png',])).convert_alpha()
        
  
    def update(self):
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance > self.speed:
            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed
        self.rect.center = (self.x, self.y)

    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
        pygame.display.flip()

    def set_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

    def get_enermy_rect(self):
        enermyrect = pygame.Rect(self.x,self.y,16,16)
        return enermyrect


