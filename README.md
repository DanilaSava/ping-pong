# ping-pong
v 1.2


from pygame import *
mixer.init()
font.init()
from random import randint
from time import time as timer


window = display.set_mode((700, 393))


clock = time.Clock()
FPS = 60






background = transform.scale(image.load("field.png"), (700, 393))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, width, height, speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        self.width = width
        self.height = height
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):

        
    def update(self):
        
        keys_pressed = key.get_pressed()

        if keys_pressed [K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed [K_s] and self.rect.y < 250:
            self.rect.y += self.speed

    def update1(self):
        
        keys_pressed = key.get_pressed()

        if keys_pressed [K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed [K_DOWN] and self.rect.y < 250:
            self.rect.y += self.speed







class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 510:
            self.rect.x = randint(0, 600)
            self.rect.y = -20
            lost = lost + 1




ball = GameSprite("ball.png", 50, 50, 7, 340, 163)

player1 = Player("player1.png", 40, 150, 10, 0, 163)
player2 = Player("player2.png", 55, 150, 10, 660, 163)


game = True

finish = False
speed_x = 3
speed_y = 3
schetP1 = 0
schetP2 = 0

font1 = font.SysFont("colibri", 35)
win1 = font1.render("!!игрок 1 победил!!", True, (100, 0, 0))
win2 = font1.render("!!игрок 2 победил!!", True, (100, 0, 0))

while game:


    for e in event.get():
        if e.type == QUIT:
            game = False
        


    if finish != True:
        

        ball.rect.y += speed_y
        ball.rect.x += speed_x

        window.blit(background,(0, 0))
    

        schet1 = font1.render("Счет игрока 1: " + str(schetP1), True,(100, 0, 0))
        schet2 = font1.render("Счет игрока 2: " + str(schetP2), True,(100, 0, 0))
        
        window.blit(schet1,(10, 10))
        window.blit(schet2,(500, 10))

        player1.update()
        player1.reset()
        player2.update1()
        player2.reset()
        ball.update()
        ball.reset()


    if ball.rect.y > 343 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1


    if ball.rect.x < 0:
        schetP2 += 1
        ball = GameSprite("ball.png", 50, 50, 7, 340, 163)
    
    if ball.rect.x > 750:
        schetP1 += 1
        ball = GameSprite("ball.png", 50, 50, 7, 340, 163)

    if schetP1 > 2:
        window.blit(win1, (230, 180))
        finish = True

    if schetP2 > 2:
        window.blit(win2, (230, 180))
        finish = True



    clock.tick(FPS)
    display.update()

    



