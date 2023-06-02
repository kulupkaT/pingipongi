from pygame import *
font.init()
mixer.init()
clock = time.Clock()
window = display.set_mode((1000,700))
background = transform.scale(image.load('istockphoto-879818534-170667a.jpg'), (1000,700))
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size1,size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 700 -80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 700 -80:
            self.rect.y += self.speed
a1 = Player('rocket.png', 50, 100, 20, 65, 200)
a2 = Player('rocket.png', 900, 300, 20, 65, 200)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        a1.update_l()
        a1.reset()
        a2.update_r()
        a2.reset()
        
        display.update()
        clock.tick(FPS)


 
    




        
