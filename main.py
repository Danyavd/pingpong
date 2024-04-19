from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('backgroundjpg.webp'), (700,500))
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed_player, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_player = speed_player
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed_player
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed_player
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed_player
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed_player




pl1 =Player('player.png', 680, 200, 5, 20, 150)
pl2 =Player2('player.png', 0, 200, 5, 20, 150)
ball = GameSprite('i.webp', 350, 200, 5, 50, 50)

clock = time.Clock()
FPS = 60
sped_x=5
speed_y=3
font2 = font.Font(None, 70)

lose = font2.render('You lose', True, (255, 0, 0))

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    pl1.reset()
    pl1.update()
    pl2.reset()
    pl2.update()
    ball.reset()
    ball.update()
    ball.rect.x += sped_x
    ball.rect.y += speed_y
    if sprite.collide_rect(pl1,ball) or sprite.collide_rect(pl2,ball):
        sped_x *= -1
        speed_y *= 1
    if ball.rect.y>=win_height:
        speed_y *= -1
    if ball.rect.y<=0:
        speed_y *= -1
    if ball.rect.x >= win_width:
        window.blit(lose, (win_width/2,win_height/2))
    if ball.rect.x <= 0:
        window.blit(lose, (win_width/2,win_height/2))

    display.update()
    clock.tick(FPS)


