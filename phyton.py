from pygame import *
mixer.init()
font.init()
from random import randint
from time import time as timer


window = display.set_mode((700, 393))


clock = time.Clock()
FPS = 120


speed_x = 3
speed_y = 3



#k = mixer.Sound("ping-pong.mp3")
#q = mixer.Sound("ping-pong2.mp3")


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

        if keys_pressed [K_s] and self.rect.y < 350:
            self.rect.y += self.speed

  

    def update1(self):
        
        keys_pressed = key.get_pressed()

        if keys_pressed [K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed [K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, width, height, speed, player_x, player_y, speed_x, speed_y):
        super().__init__(player_image, width, height, speed, player_x, player_y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        ball.rect.y += self.speed_y
        ball.rect.x += self.speed_x
 

    def hit(self, paddle):
        if sprite.collide_rect(self, paddle):
            #k.play()
            angle = section(paddle, self)
            if abs(angle) == 40:
                self.speed_x = 3
                self.speed_y = 3
            elif abs(angle) == 20:
                self.speed_x = 3
                self.speed_y = 1
            elif abs(angle) == 0:
                self.speed_x = 3
                self.speed_y = 0
            if angle < 0:
                self.speed_y *= -1
            if self.rect.x >= 450:
                self.speed_x *= -1






def section (paddle, pong):
    height = paddle.rect.bottom - paddle.rect.top 
    if pong.rect.centery <= (paddle.rect.y + height * 1/4):
        return -40
    elif pong.rect.centery <= (paddle.rect.y + height * 2/5):
        return -20
    elif pong.rect.centery <= (paddle.rect.y + height * 3/5):
        return 0
    elif pong.rect.centery <= (paddle.rect.y + height * 4/5):
        return 20
    elif pong.rect.centery <= (paddle.rect.y + height * 5/5):
        return 40









ball = Ball("ball.png", 50, 50, 7, 340, 163, 2, 2)

player1 = Player("player1.png", 40, 150, 1, 0, 163)
player2 = Player("player2.png", 55, 150, 1, 660, 163)


game = True

finish = False







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
        



        window.blit(background,(0, 0))
    

        schet1 = font1.render("Счет игрока 1: " + str(schetP1), True,(100, 0, 0))
        schet2 = font1.render("Счет игрока 2: " + str(schetP2), True,(100, 0, 0))
        
        window.blit(schet1,(10, 10))
        window.blit(schet2,(500, 10))




        if ball.rect.y > 343 or ball.rect.y < 0:
            ball.speed_y *= -1




        if schetP1 > 10 and schetP1 - schetP2 >= 2:
            window.blit(win1, (230, 180))
            finish = True

        if schetP2 > 10 and schetP2 - schetP1 >= 2:
            window.blit(win2, (230, 180))
            finish = True


        if ball.rect.x < -50:
            schetP2 += 1
            ball.kill()
            ball = Ball("ball.png", 50, 50, 7, 340, 163, 1, 1)

        
        if ball.rect.x > 800:
            schetP1 += 1
            ball.kill()
            ball = Ball("ball.png", 50, 50, 7, 340, 163, 1, 1)

        

        ball.hit(player1)
        ball.hit(player2)
        ball.update()
        ball.reset() 
        player1.update()
        player1.reset()
        player2.update1()
        player2.reset()




    clock.tick(FPS)
    display.update()

    


    

    



