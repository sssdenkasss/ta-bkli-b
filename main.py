
from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
game = True
clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
w1 = Wall(154, 205, 50, 100, 20, 600, 10)
w2 = Wall(154, 205, 50, 100, 20, 10, 380)
w3 = Wall(154, 205, 50, 410, 20, 10, 160)
w4 = Wall(154, 205, 50, 300, 450, 400, 10)
w5 = Wall(154, 205, 50, 100, 230, 480, 10)
w6 = Wall(154, 205, 50, 250, 40, 10, 210)
w7 = Wall(154, 205, 50, 250, 180, 105, 10)
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 3)
goal = GameSprite('treasure.png', 150, 150, 0)
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
font.init()
font1 = font.Font(None, 100)
win = font1.render('YOU WIN!!!', True, (255, 215, 0))
lose = font1.render('GAME OVER!!!',True, (255, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    player.update()
    monster.update()
    goal.reset()
    player.reset()
    monster.reset()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()
    if sprite.collide_rect(player, goal):
        window.blit(win, (200, 200))
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or\
        sprite.collide_rect(player, w2) or \
        sprite.collide_rect(player, w3) or \
        sprite.collide_rect(player, w4) or \
        sprite.collide_rect(player, w5) or \
        sprite.collide_rect(player, w6) or \
        sprite.collide_rect(player, w7):
        window.blit(lose, (200,200))


    display.update()
    clock.tick(FPS)
