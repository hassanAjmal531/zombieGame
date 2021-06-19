import pygame as p
import math as m

p.init()
window = p.display.set_mode((1400, 700))
window.fill((255, 255, 255))
frame_rate = p.time.Clock()

# loading images of the player
walkRightarr = [p.image.load('R1.png'), p.image.load('R2.png'), p.image.load('R3.png'), p.image.load('R4.png'),
                p.image.load('R5.png'), p.image.load('R6.png'), p.image.load('R7.png'), p.image.load('R8.png'),
                p.image.load('R9.png')]
walkLeftarr = [p.image.load('L1.png'), p.image.load('L2.png'), p.image.load('L3.png'), p.image.load('L4.png'),
               p.image.load('L5.png'), p.image.load('L6.png'), p.image.load('L7.png'), p.image.load('L8.png'),
               p.image.load('L9.png')]
bg = p.image.load('bg1.jpg')
char = p.image.load('standing.png')
collision = False
collision1 = False
score = 0


class screen_objects(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x1 = self.x
        self.y1 = self.y
        self.hWidth = self.width
        self.hHeight = self.height
        self.hitbox = [self.x1 - 10, self.y - 7, self.hWidth + 20, self.hHeight + 12]

    def draw_box(self):
        p.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        p.draw.rect(window, (0, 0, 0), (self.x, self.y, self.width, self.height))


class projectile_bullets(object):
    def __init__(self, x, y, r, facing):
        self.x = x
        self.y = y
        self.radius = r
        self.color = (0, 0, 0)
        self.face = facing
        self.vel = 20 * facing

    def draw_bullets(self, window):
        p.draw.circle(window, self.color, (self.x, self.y), self.radius)

class player(object):
    def __init__(self):
        self.x = 100
        self.y = 640
        self.width = 64
        self.height = 64
        self.vel = 10
        self.walk_right = False
        self.walk_left = False
        self.jump = 10
        self.in_jump = False
        self.walkframe = 0
        self.stationary = True
        self.hitbox = [self.x + 20, self.y, 28, 60]
        self.visibilltiy = True
        self.h_width = 120
        self.hitbox = (self.x + 17, self.y + 11, 27, 52)
        self.a = self.hitbox[3] - self.hitbox[1]

    def move(self, window):
        if self.walkframe + 1 >= 27:
            self.walkframe = 0
        if not (self.stationary):
            if self.walk_right:
                window.blit(walkRightarr[self.walkframe // 3], (self.x, self.y))
                self.walkframe += 1
            elif self.walk_left:
                window.blit(walkLeftarr[self.walkframe // 3], (self.x, self.y))
                self.walkframe += 1
        else:
            if self.walk_right:
                window.blit(walkRightarr[0], (self.x, self.y))
                self.walkframe = 0
            elif self.walk_left:
                window.blit(walkLeftarr[0], (self.x, self.y))
                self.walkframe = 0
        self.hitbox = (self.x + 17, self.y + 11, 27, 52)
        #p.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    def collision(self):
        print("hit")


class goblins(object):
    walkRight = [p.image.load('R1E.png'), p.image.load('R2E.png'), p.image.load('R3E.png'),
                 p.image.load('R4E.png'), p.image.load('R5E.png'), p.image.load('R6E.png'),
                 p.image.load('R7E.png'), p.image.load('R8E.png'), p.image.load('R9E.png'),
                 p.image.load('R10E.png'), p.image.load('R11E.png')]
    walkLeft = [p.image.load('L1E.png'), p.image.load('L2E.png'), p.image.load('L3E.png'),
                p.image.load('L4E.png'), p.image.load('L5E.png'), p.image.load('L6E.png'),
                p.image.load('L7E.png'), p.image.load('L8E.png'), p.image.load('L9E.png'),
                p.image.load('L10E.png'), p.image.load('L11E.png')]

    def __init__(self,x,y,width,height,path,vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = path
        self.walkframe = 0
        self.vel = vel
        self.health = 100
        self.h_width = 27
        self.visibilty = True
        self.hitbox = (self.x + 17, self.y + 11, 27, 52)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel *= -1
                self.x += self.vel
                self.walkframe = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel *= -1
                self.x += self.vel
                self.walkframe = 0

    def draw_enemy(self):
        if self.visibilty:

            self.move()
            if self.walkframe + 1 >= 33:
                self.walkframe = 0
            else:
                if self.vel > 0:
                    window.blit(self.walkRight[self.walkframe // 3], (self.x, self.y))
                    self.walkframe += 1
                else:
                    window.blit(self.walkLeft[self.walkframe // 3], (self.x, self.y))
                    self.walkframe += 1
        self.hitbox = (self.x + 17, self.y + 11, 27, 52)
        p.draw.rect(window, (255, 0, 0), self.hitbox, 2)
          #  p.draw.rect(window, (255, 0, 0), (self.x + 10, self.y - 10, 27, 5))
           # p.draw.rect(window, (12, 138, 12), (self.x + 10, self.y - 10, self.h_width, 5))


def draw():
    window.fill((255, 255, 255))
    box1.draw_box()
    box2.draw_box()
    box3.draw_box()
    box4.draw_box()
    box5.draw_box()
    #box_surface.draw_box()
    viking.move(window)
    for bullet in bullets:
        bullet.draw_bullets(window)
    enemy_zombie.draw_enemy()
    enemy_zombie1.draw_enemy()
    enemy_zombie2.draw_enemy()
    enemy_zombie3.draw_enemy()
    p.display.update()


box1 = screen_objects(0, 300, 350, 20)
box2 = screen_objects(1000, 400, 400, 20)
box3 = screen_objects(580, 630, 300, 70)
box4 = screen_objects(620, 580, 200, 60)
box5 = screen_objects(670, 520, 120, 70)
#box_surface = screen_objects(0, 650, 1400, 50)

bullets = []
enemy_zombie = goblins(20,640,64,64,[20,500],3)
enemy_zombie1 = goblins(650,640,64,64,[880,1350],4)
enemy_zombie2 = goblins(20,245,64,64,[20,300],3)
enemy_zombie3 = goblins(1000,345,64,64,[1020,1350],3)

viking = player()
run = True
while run:
    frame_rate.tick(27)
    # checking collision wth the boxes

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    keys = p.key.get_pressed()
    for bullet in bullets:
        if bullet.y - bullet.radius < enemy_zombie.hitbox[1] + enemy_zombie.hitbox[3] and bullet.y + bullet.radius > \
                enemy_zombie.hitbox[1]:
            if bullet.x + bullet.radius > enemy_zombie.hitbox[0] and bullet.x - bullet.radius < enemy_zombie.hitbox[0] + \
                    enemy_zombie.hitbox[2]:
                bullets.pop(bullets.index(bullet))
                score += 1
                # to decrease health
                enemy_zombie.h_width -= 1
                viking.collision()

        elif bullet.y - bullet.radius < enemy_zombie1.hitbox[1] + enemy_zombie1.hitbox[
            3] and bullet.y + bullet.radius > \
                enemy_zombie1.hitbox[1]:
            if bullet.x + bullet.radius > enemy_zombie.hitbox[0] and bullet.x - bullet.radius < \
                    enemy_zombie1.hitbox[0] + \
                    enemy_zombie1.hitbox[2]:
                bullets.pop(bullets.index(bullet))
                score += 1
                # to decrease health
                enemy_zombie.h_width -= 1
                viking.collision()

        elif bullet.y - bullet.radius < enemy_zombie2.hitbox[1] + enemy_zombie2.hitbox[
            3] and bullet.y + bullet.radius > \
                enemy_zombie2.hitbox[1]:
            if bullet.x + bullet.radius > enemy_zombie1.hitbox[0] and bullet.x - bullet.radius < \
                    enemy_zombie2.hitbox[0] + \
                    enemy_zombie2.hitbox[2]:
                bullets.pop(bullets.index(bullet))
                score += 1
                # to decrease health
                enemy_zombie2.h_width -= 1
                viking.collision()

        elif bullet.y - bullet.radius < enemy_zombie3.hitbox[1] + enemy_zombie3.hitbox[
            3] and bullet.y + bullet.radius > \
                enemy_zombie3.hitbox[1]:
            if bullet.x + bullet.radius > enemy_zombie3.hitbox[0] and bullet.x - bullet.radius < \
                    enemy_zombie3.hitbox[0] + \
                    enemy_zombie3.hitbox[2]:
                bullets.pop(bullets.index(bullet))
                score += 1
                # to decrease health
                enemy_zombie3.h_width -= 1
                viking.collision()
                if enemy_zombie3.h_width == 0:
                    enemy_zombie3.visibilty = False

        if 1400 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    if keys[p.K_SPACE]:

        if viking.walk_left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile_bullets(round(viking.x + viking.width // 2),
                                   round(viking.y + viking.height // 2), 6, facing))

    #if math.sqrt((viking.x+viking )):

    if keys[p.K_RIGHT] and viking.x < 1400 - viking.vel:
        viking.walk_right = True
        viking.walk_left = False
        viking.stationary = False
        viking.x += viking.vel
    elif keys[p.K_LEFT] and viking.x > 20 - viking.vel:
        viking.walk_left = True
        viking.walk_right = False
        viking.stationary = False
        viking.x -= viking.vel

    else:
        viking.stationary = True
    if not (viking.in_jump):

        if keys[p.K_UP]:
            viking.in_jump = True
    else:

        if viking.jump >= -10:
            neg = 1
            if viking.jump < 0:
                neg = -1
                # using eqaution of parabola
            viking.y -= (viking.jump ** 2) * 0.5 * neg
            viking.jump -= 1
        else:
            viking.in_jump = False
            viking.jump = 10

    draw()
p.quit()
