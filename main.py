from rzeznik import *


def napisz(tekst, x=0, y=0, rozmiar=30, r=255, g=255, b=255):
    cz = pygame.font.SysFont("Arial", rozmiar)
    rend = cz.render(tekst, 1, (r,g,b))
    x1 = (szer - rend.get_rect().width )/2 +x
    y1 = (wys - rend.get_rect().height)/2 +y
    screen.blit(rend, (x1,y1))

#------------------------------------------------------------------------
#General setup

clock = pygame.time.Clock()

timer_rctrl_first = 0
timer_rctrl_second = 0
timer_rshift = 0
#Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Rzeznik(dx,dy)
moving_sprites.add(player)

#Character
player.direction = "right"

#-------------------------------------------------------------
key = pygame.key.get_pressed()
while key[pygame.K_SPACE] == False:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    time_elapsed = int(pygame.time.get_ticks()/1000)
    font = pygame.font.SysFont('Arial', 18)
    napisz('{} s'.format(time_elapsed),szer/2-30,-wys/2+20,15)

    if time_elapsed > 0:
        napisz("Czasy średniowieczne", 0,-140,70,255,255,255)
    if time_elapsed > 1.3:
        napisz("Na ludzi napadają wiedźmy i słowiańskie potwory", 0, -80,40,255,255,255)
    if time_elapsed > 2.5:
        napisz("Jesteś SĘDZIĄ, ", -265, 30,40,255,255,255) 
    if time_elapsed > 3.3:
        napisz("ŁAWĄ PRZYSIĘGŁYCH", 25, 30,40,255,255,255) 
    if time_elapsed > 4.4:
        napisz(" i   KATEM", 295,30,40,240,15,15) 
    if time_elapsed >5:# 2.5:
        napisz("Nacisnij SPACJE zeby zaczac", 0, 200, 30, 190,190,190)
    
    key = pygame.key.get_pressed()
    pygame.display.flip()
#------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:
                print("RCTRL")
                if time_elapsed > timer_rctrl_first + 700:
                    print(time_elapsed)
                    print(timer_rctrl_first)
                    if player.direction != "fight":
                        player.before_direction = player.direction
                    player.direction = "fight"
                    timer_rctrl_first = time_elapsed
            if event.key == pygame.K_RSHIFT:
                print("RSHIFT")
                timer_rshift =  time_elapsed
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                print("W")
                player.jumping = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                print("S")
                falling = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                print("A")
                player.direction = "runleft"
                dx=-move_speed
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print("D")
                player.direction = "runright"
                dx=move_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RCTRL:
                #print(time_elapsed - timer_rctrl_first)
                player.direction = player.before_direction
                #timer_rctrl_first = 0
            if event.key == pygame.K_RSHIFT:
                print(time_elapsed - timer_rshift)
                timer_rshift = 0
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if dx != 2:
                    dx=0
                    player.direction = "left"
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if dx != -2:
                    dx=0
                    player.direction = "right"


    player.ruch(dx,dy)
    
    #bg = pygame.image.load("wall.png")
    #screen.blit(bg, (0, 0))

    key = pygame.key.get_pressed()    
    time_elapsed = pygame.time.get_ticks()
    

    #Drawing
    screen.fill((190,190,190))
    moving_sprites.draw(screen)
    moving_sprites.update(0.07)
    platform_group.draw(screen)

    pygame.display.flip()
    clock.tick(100)