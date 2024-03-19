import pygame, sys, time, os, random

pygame.init()

szer = 1000
wys = 600

#jumping = False
falling = False

dx = 0
dy = wys-120
move_speed = 3

screen = pygame.display.set_mode((szer,wys))
pygame.display.set_caption('Boskie wyroki')



class Rzeznik(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()

        self.jump_height = 18
        self.gravity = 1
        self.velocity = self.jump_height
        self.on_ground = True

        
        self.direction = "right"
        self.before_direction = "right"
        self.jumping = False
        self.kolizja = False

        self.bat_enemy = True

        self.width = 90
        self.height = 120
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = (pos_x,pos_y)

        self.bat_rect = pygame.Rect(0,0,self.width, self.height)
        self.bat_rect.center = (szer-100,pos_y)

        self.sprites = []
        self.sprites_left = []
        self.sprites_right_run=[]
        self.sprites_left_run =[]
        self.sprites_fight = []
        self.sprites_bat = []
        self.sprites_bat_left = []

        self.sprites.append(pygame.image.load('wojownik_normal_right-1.png'))
        self.sprites.append(pygame.image.load('wojownik_normal_right-2.png'))
        self.sprites.append(pygame.image.load('wojownik_normal_right-3.png'))
        self.sprites.append(pygame.image.load('wojownik_normal_right-4.png'))
        self.sprites.append(pygame.image.load('wojownik_normal_right-5.png'))
        self.sprites.append(pygame.image.load('wojownik_normal_right-6.png'))
        self.sprites_left.append(pygame.image.load('wojownik_normal_left-1.png'))
        self.sprites_left.append(pygame.image.load('wojownik_normal_left-2.png'))
        self.sprites_left.append(pygame.image.load('wojownik_normal_left-3.png'))
        self.sprites_left.append(pygame.image.load('wojownik_normal_left-4.png'))
        self.sprites_left.append(pygame.image.load('wojownik_normal_left-5.png'))
        self.sprites_left.append(pygame.image.load('wojownik_normal_left-6.png'))
        self.sprites_right_run.append(pygame.image.load('wojownik_run_right-1.png'))
        self.sprites_right_run.append(pygame.image.load('wojownik_run_right-2.png'))
        self.sprites_right_run.append(pygame.image.load('wojownik_run_right-3.png'))
        self.sprites_right_run.append(pygame.image.load('wojownik_run_right-4.png'))
        self.sprites_right_run.append(pygame.image.load('wojownik_run_right-5.png'))
        self.sprites_right_run.append(pygame.image.load('wojownik_run_right-6.png'))
        self.sprites_left_run.append(pygame.image.load('wojownik_run_left-1.png'))
        self.sprites_left_run.append(pygame.image.load('wojownik_run_left-2.png'))
        self.sprites_left_run.append(pygame.image.load('wojownik_run_left-3.png'))
        self.sprites_left_run.append(pygame.image.load('wojownik_run_left-4.png'))
        self.sprites_left_run.append(pygame.image.load('wojownik_run_left-5.png'))
        self.sprites_left_run.append(pygame.image.load('wojownik_run_left-6.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight1.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight2.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight3.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight4.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight5.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight6.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight7.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight8.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight9.png'))
        self.sprites_fight.append(pygame.image.load('wojownik_fight10.png'))
        self.sprites_bat.append(pygame.image.load('bat1.png'))
        self.sprites_bat.append(pygame.image.load('bat2.png'))
        self.sprites_bat.append(pygame.image.load('bat3.png'))
        self.sprites_bat.append(pygame.image.load('bat4.png'))
        # self.sprites_bat_left.append(pygame.image.load('bat1leftt.png'))
        # self.sprites_bat_left.append(pygame.image.load('bat2leftt.png'))
        # self.sprites_bat_left.append(pygame.image.load('bat3leftt.png'))
        # self.sprites_bat_left.append(pygame.image.load('bat4leftt.png'))

        self.current_sprite = 0
        self.current_sprite_left = 0
        self.current_sprite_run_right = 0
        self.current_sprite_run_left = 0
        self.current_sprite_fight = 0
        self.current_sprite_bat = 0
        self.current_sprite_bat_left = 0

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

        self.image_enemy = self.sprites_bat[self.current_sprite_bat]



    def update(self, speed):

        if self.direction == "right":
            self.image = self.sprites[int(self.current_sprite)]
        elif self.direction == "left":
            self.image = self.sprites_left[int(self.current_sprite_left)]
        elif self.direction == "runright":
            self.image = self.sprites_right_run[int(self.current_sprite_run_right)]
        elif self.direction == "runleft":
            self.image = self.sprites_left_run[int(self.current_sprite_run_left)]
        elif self.direction == "fight":
            self.image = self.sprites_fight[int(self.current_sprite_fight)]


        if self.direction in ["right", "left", "runright", "runleft", "fight"]:

            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
            self.current_sprite_left += speed
            if int(self.current_sprite_left) >= len(self.sprites_left):
                self.current_sprite_left = 0
            self.current_sprite_run_right += speed
            if int(self.current_sprite_run_right) >= len(self.sprites_right_run):
                self.current_sprite_run_right = 0
            self.current_sprite_run_left += speed
            if int(self.current_sprite_run_left) >= len(self.sprites_left_run):
                self.current_sprite_run_left  = 0

            self.current_sprite_fight += 0.5
            if int(self.current_sprite_fight) >= len(self.sprites_fight):
                self.current_sprite_fight = 0
                # self.direction = "right "
                #self.direction = self.before_direction


            if self.bat_enemy == True:
                self.image_enemy = self.sprites_bat[int(self.current_sprite_bat)]
                self.current_sprite_bat += 0.15
                if int(self.current_sprite_bat) >= len(self.sprites_bat):
                    self.current_sprite_bat = 0


    def ruch(self, u, v):
        #global jumping
        global dy

        #jesli pionowa kolizja z platforma to podniesie gracza do gory
        # while self.kolizja:
        #     dy -= 1
        #     if not any(platform.rect.colliderect(self.rect) for platform in platform_group):
        #         self.kolizja = False
        # self.on_ground = True

        # stała grawitacja
        if not self.jumping or falling:
            dy += self.velocity
            #print("grawitacja w dol")
        elif self.jumping:
            self.on_ground = False
            dy -= self.velocity
            self.velocity -= self.gravity
            if self.velocity < -self.jump_height:
                self.jumping = False
                self.velocity = self.jump_height
        

        # Ruch poziomy i kolizje z krawędziami ekranu
        if self.rect.x + u < 0:
            u = -self.rect.x
        elif self.rect.x + u > szer - 90:
            u = szer - self.rect.x
        else:
            self.rect.x += u  


        self.on_ground = False 
        for platform in platform_group:
            if (platform.rect.colliderect(self.rect)) and (self.rect.bottom - platform.rect.top < 20): 
                if (self.velocity <= 0 and self.jumping == True) or (self.velocity== self.jump_height and self.jumping == False): 
                    #warunki: kolizja, postac ponad platforma generalnie, spada(po skoku lub z grawitacji)
                    print("kolizja1")
                    print(self.rect.bottom)
                    print(platform.rect.top)
                    print("---")
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.jumping = False
                    self.velocity = self.jump_height
            elif platform.rect.top == self.rect.bottom and self.jumping == False and (platform.rect.left < self.rect.left + self.width) and (platform.rect.right + self.width > self.rect.right):
                # print("k2")
                self.on_ground = True

        # Ograniczenie dolnej granicy ekranu
        if dy > wys - 120:
            dy = wys - 120

        if self.on_ground == False:
            self.rect.y = dy 
        
        dy = self.rect.y



class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        ground_image = pygame.image.load('ground.png').convert_alpha()
        self.image = pygame.transform.scale(ground_image, (width, 18))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

platform_group = pygame.sprite.Group()
for p in range(5):
    p_w = 150
    p_x = random.randint(0,szer - p_w)
    p_y = random.randint(500,wys)
    platform = Platform(p_x, p_y, p_w)
    platform_group.add(platform)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemy_image = pygame.image.load('bat1.png')
