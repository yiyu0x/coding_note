#-*-coding:utf-8-*-
import pygame
import random
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((10,20))
        self.surf.fill((random.randint(30,255),random.randint(30,255),random.randint(30,255)))
        self.rect = self.surf.get_rect(center=(random.randint(0,400),0))
        self.speed = random.randint(5,10)

    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.right < 0:
            self.kill()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(200,700))
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 400:
            self.rect.right = 400
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 700:
            self.rect.bottom = 700

pygame.init()

screen = pygame.display.set_mode((400,700))
pygame.display.set_caption("pygame practice")
player = Player()


enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


ADDENEMY = pygame.USEREVENT+1
#generation time
pygame.time.set_timer(ADDENEMY,200)

running = True

score = 0

while running:
    score += 1
    for event in pygame.event.get():
        # check for KEYDOWN event: KEYDOWN is a constant defined in pygame.locals,which we imported earlier
        if event.type == KEYDOWN:
            # if the Esc KEY has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
            # check for QUIT event: if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)



    screen.fill((0,0,0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)  
    enemies.update() 
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        # player.kill()
        running = False
        print "Game Over !!!"
        print "your score is : ",score
        print "good bye ~ "

    screen.blit(player.surf,player.rect)



    pygame.display.flip()
