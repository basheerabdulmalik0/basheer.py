# بسم الله نبدأ

import pygame
import random

pygame.init()

# defining the screen

win = pygame.display.set_mode((700,650))
icon = pygame.image.load("icon.png")

pygame.display.set_caption("Bouncy")
pygame.display.set_icon(icon)

# the user's variables :

x = 290
y = 610
width = 120
height = 16
vel = 5
isjump = False
jumpcount = 10
jumpcount = int(jumpcount)
user_rect = pygame.Rect(x, y, width, height)

# colors :

gray = (50,50,50)
fire = (100,0,0)
win_color = (250, 250, 250)
side_bars_color = (100,100,100)
ur_color = (0,0,0)
score_color = (0,0,0)
collider_color = (180,180,180)

dark_mode = False

# moving rect :

x_speed = 4
y_speed = 3
x_position = random.randint(200, 500)
y_position = random.randint(200, 400)
moving_rect = pygame.Rect(x_position, y_position, 30, 30)

# clone rect :

clone_x_speed = 4
clone_y_speed = 3
clone_x = 1000
clone_y = 1000
clone_rect = pygame.Rect(clone_x, clone_y, 30, 30)
cloning = False
re_cloning = False

# side bars :

top_speed = 2
top_x = random.randint(100,500)
top_rect = pygame.Rect(top_x, 0, 200, 11)

right_speed = 3
right_y = random.randint(100,400)
right_rect = pygame.Rect(689,right_y,11,100)

left_speed = 3
left_y = random.randint(100,400)
left_rect = pygame.Rect(0,left_y,11,100)

tl_rect = pygame.Rect(30,30,5,90)
tr_rect = pygame.Rect(665,30,5,90)
t_rect_speed = 1

# music :

pygame.mixer.music.load("song.wav")
game_music = False
final_score = pygame.mixer.Sound("goal.wav")
boo = pygame.mixer.Sound("boo.wav")

# score :

score = 0
font = pygame.font.SysFont("Papyrus", 17)

# fonts :

title_font = pygame.font.SysFont("Papyrus", 50)
large_font = pygame.font.SysFont("Papyrus", 100)
small_font = pygame.font.SysFont("Papyrus", 25, True)

# shapes :

def shapes() :

    global x_speed , y_speed, image
    global top_x, right_y, left_y, top_speed, right_speed, left_speed,t_rect_speed
    global color, clone_color, gray, fire
    global clone_x_speed, clone_y_speed, cloning, re_cloning
    global score
    global side_bars_color, ur_color, collider_color, win_color, score_color 
    
    if dark_mode == True :
        gray = (205, 205, 205)
        fire = (200, 0, 0)
        win_color = (5, 5, 5)
        side_bars_color = (155, 155, 155)
        ur_color = (100, 100, 100)
        
        collider_color = (75, 75, 75)

    elif dark_mode == False :
        gray = (50, 50, 50)
        fire = (100, 0, 0)
        win_color = (250, 250, 250)
        side_bars_color = (100, 100, 100)
        ur_color = (0, 0, 0)
        collider_color = (180, 180, 180)


    # top side :
    
    pygame.draw.rect(win, side_bars_color, (0,0,700,10))
    pygame.draw.rect(win, collider_color, top_rect)

    top_rect.x += top_speed

    if top_rect.right >= 700 or top_rect.left <= 0 :
        top_speed *= -1

    if moving_rect.colliderect(top_rect) :
        score += 20
        color = fire
        x_speed *= -1

        if x_speed > 0 :
            x_speed += 3

        if x_speed < 0 :
            x_speed -= 3

        y_speed += 1


    if clone_rect.colliderect(top_rect) :
        score += 20
        clone_color = fire
        clone_x_speed *= -1

        if clone_x_speed > 0 :
            clone_x_speed += 3 

        if clone_x_speed < 0 :
            clone_x_speed -= 3

        clone_y_speed += 1

    
    # left side :
    
    pygame.draw.rect(win, side_bars_color, (0,0,10,610))
    pygame.draw.rect(win, collider_color, left_rect)

    left_rect.y += left_speed

    if left_rect.top <= 0 or left_rect.bottom >= 610 :
        left_speed *= -1

    if moving_rect.colliderect(left_rect) :
        score += 25
        color = fire
        y_speed *= -1

        if y_speed > 0 :
            y_speed += 2

        if y_speed < 0 :
            y_speed -= 2


    if clone_rect.colliderect(left_rect) :
        score += 25
        clone_color = fire
        clone_y_speed *= -1

        if clone_y_speed > 0 :
            clone_y_speed += 2

        if clone_y_speed < 0 :
            clone_y_speed -= 2
    
    # right side :
    
    pygame.draw.rect(win, side_bars_color, (690,0,10,610))
    pygame.draw.rect(win, collider_color, right_rect)

    right_rect.y += right_speed

    if right_rect.top <= 0 or right_rect.bottom >= 610 :
        right_speed *= -1

    if moving_rect.colliderect(right_rect) :
        score += 25
        color = fire
        y_speed *= -1

        if y_speed > 0 :
            y_speed += 2

        if y_speed < 0 :
            y_speed -= 2


    if clone_rect.colliderect(right_rect) :
        score += 25
        clone_color = fire
        clone_y_speed *= -1

        if clone_y_speed > 0 :
            clone_y_speed += 2

        if clone_y_speed < 0 :
            clone_y_speed -= 2

    # the user's bar :
    
    pygame.draw.rect(win, ur_color, user_rect)

    # transportation bars :

    pygame.draw.rect(win, (255,0,0), tl_rect)
    pygame.draw.rect(win, (255,0,0), tr_rect)

    tl_rect.y += t_rect_speed
    tr_rect.y += t_rect_speed

    if tl_rect.bottom >= 600 or tl_rect.top <= 10 :
        t_rect_speed *= -1

    if moving_rect.colliderect(tl_rect) and x_speed < 0:
        score += 25
        moving_rect.x += 620

    if moving_rect.colliderect(tr_rect) and x_speed > 0 :
        score += 25
        moving_rect.x -= 620


    if clone_rect.colliderect(tl_rect) and clone_x_speed < 0 :
        score += 25
        clone_rect.x += 620

    if clone_rect.colliderect(tr_rect) and clone_x_speed > 0 :
        score += 25
        clone_rect.x -= 620
    

    # the moving rect :

    pygame.draw.circle(win, color, (moving_rect.x + 15,moving_rect.y + 15),15,0)
    
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    if moving_rect.right >= 690 or moving_rect.left <= 10 :
        x_speed *= -1

    if moving_rect.top <= 10 :
        y_speed *= -1

    if moving_rect.x >= 1000 or moving_rect.y >= 1000 :
        re_cloning = True
        
        y_speed = abs(y_speed)
        moving_rect.y += y_speed

        x_speed = abs(x_speed)
        moving_rect.x += x_speed

    if (clone_rect.colliderect(user_rect)) and (isjump == True) :

        if score >= 300 and moving_rect.y >= 1000 :
            score -= 250

        if re_cloning == True :
            moving_rect.x = clone_rect.x
            moving_rect.y = clone_rect.y
            
            x_speed = clone_x_speed * -1
            re_cloning = False

    # the clone rect :

    pygame.draw.circle(win, clone_color, (clone_rect.x + 15,clone_rect.y + 15),15,0)

    if clone_rect.x >= 1000 or clone_rect.y >= 1000 :
        cloning = True
    
        clone_y_speed = abs(clone_y_speed)
        clone_rect.y += clone_y_speed

        clone_x_speed = abs(clone_x_speed)
        clone_rect.x += clone_x_speed

    if (moving_rect.colliderect(user_rect) and isjump == True) :

        if score >= 300 and clone_rect.y >= 1000 :
            score -= 250

        if cloning == True :
            clone_rect.x = moving_rect.x
            clone_rect.y = moving_rect.y
            
            clone_x_speed = x_speed * -1
            cloning = False
            
    clone_rect.x += clone_x_speed   
    clone_rect.y += clone_y_speed

    if clone_rect.right >= 690 or clone_rect.left <= 10 :
        clone_x_speed *= -1

    if clone_rect.top <= 10 :
        clone_y_speed *= -1

    # bouncing and collisions :

    collision_constant = 5

    if moving_rect.colliderect(user_rect) and y_speed > 0 :
        score += (abs(x_speed) + y_speed) * 10
        
        color = gray
        y_speed = 3
        y_speed *= -1
        
        if x_speed > 0 :
            x_speed = 4
            
        if x_speed < 0 :
            x_speed = -4


    if clone_rect.colliderect(user_rect) and clone_y_speed > 0 :
        score += (abs(clone_x_speed) + clone_y_speed) * 10
        
        clone_color = gray
        clone_y_speed = -3
        
        if clone_x_speed > 0 :
            clone_x_speed = 4
            
        if clone_x_speed < 0 :
            clone_x_speed = -4

    if moving_rect.y >= 650 and clone_rect.y >= 650 :
        game_over = title_font.render("GAME OVER", True, score_color)
        win.blit(game_over, (155,150))

    # score :

    if dark_mode :
        score_color = (255, 255, 255)

    else :
        score_color = (0, 0, 0)
    
    score_count = font.render("Score : " + str(score), True, score_color)
    win.blit(score_count, (10,625))

    if moving_rect.y >= 1000 and clone_rect.y >= 1000 :
        intro = True
        moving_rect.x = random.randint(200, 500)
        moving_rect.y = random.randint(200, 400)
        user_rect.x = 290
        user_rect.y = 610
        x_speed = random.choice((4,-4))
        y_speed = random.choice((3,-3))
        color = gray
        top_x = random.randint(100,500)
        right_y = random.randint(100,400)
        left_y = random.randint(100,400)
        return final_screen()
        return intro_function()


    pygame.display.update()


# button function :

def make_button(b_x, b_y, b_w, b_h, t_pos, b_t) :

    click = pygame.mouse.get_pressed() # output : (0, 0, 0)
    
    black = (250,250,250)
    bright_black = (230,230,230)
    
    mouse = pygame.mouse.get_pos()
    
    if (b_x + b_w) >= mouse[0] >= b_x and (b_y + b_h) >= mouse[1] >= b_y :
        pygame.draw.rect(win, bright_black,(b_x,b_y,b_w,b_h))
    
    else :
        pygame.draw.rect(win, black,(b_x, b_y, b_w, b_h))

    button_font = pygame.font.SysFont("Papyrus", 15, True)
    button_text = button_font.render(b_t, True, (0,0,0))
    win.blit(button_text, t_pos)


# dark button function :

def make_dark_button(b_x, b_y, b_w, b_h, t_pos, b_t) :

    click = pygame.mouse.get_pressed() # output : (0, 0, 0)
    
    black = (10,10,10)
    bright_black = (25,25,25)
    
    mouse = pygame.mouse.get_pos()
    
    if (b_x + b_w) >= mouse[0] >= b_x and (b_y + b_h) >= mouse[1] >= b_y :
        pygame.draw.rect(win, bright_black,(b_x,b_y,b_w,b_h))
    
    else :
        pygame.draw.rect(win, black,(b_x, b_y, b_w, b_h))

    button_font = pygame.font.SysFont("Papyrus", 15, True)
    button_text = button_font.render(b_t, True, (255,255,255))
    win.blit(button_text, t_pos)


# intro function :

def intro_function() :

    global large_font, title_font, small_font
    global dark_mode, game_music

    loop = 0
    loop2 = 0

    intro = True
    game_music = game_music

    while intro :

        pygame.mixer.music.pause()

        pygame.time.delay(10)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if loop > 0 :
            loop += 1

        if loop >= 5 :
            loop = 0

        if loop2 > 0 :
            loop2 += 1

        if loop2 >= 5 :
            loop2 = 0

        background = pygame.image.load("bg_4.png")
        s_bg = pygame.transform.scale(background, (700,650))
        win.blit(s_bg,(0,0))

        for event in pygame.event.get() :

            if event.type == pygame.QUIT :
                print("game over")
                pygame.quit()

        title = title_font.render("Dedicated to the special", True, (0,0,0))
        title1 = large_font.render("O",True,(0,0,0))
        title2 = small_font.render("NES",True,(0,0,0))

        creater_font = pygame.font.SysFont("Papyrus", 13)
        signature = creater_font.render("The creater, Basheer Abdulmalik : fb.com/BasheerAbdulmalik0", True, (0,0,0))
        
        win.blit(title, (90,75))
        win.blit(title1, (250,125))
        win.blit(title2,(360,215))
        win.blit(signature,(0,630))
        
        button_1_pos = (320,310)
        button_2_pos = (333,510)
        button_3_pos = (163,360)
        button_4_pos = (443,360)
        button_5_pos = (320,460)
        
        button_1 = make_button(100,300,500,40, button_1_pos, "START")
        button_2 = make_button(100,500,500,40,button_2_pos,"EXIT")
        button_3 = make_button(100,350,240,40,button_3_pos,"DARK MODE")
        button_4 = make_button(360,350,240,40,button_4_pos,"MUSIC")
        button_5 = make_button(100,450,500,40,button_5_pos,"ABOUT")

        if (100 + 500) >= mouse[0] >= 100 and (300 + 40) >= mouse[1] >= 300 :
            
            if click[0] == 1 :
                intro = False

        if (100 + 500) >= mouse[0] >= 100 and (500 + 40) >= mouse[1] >= 500 :
            
            if click[0] == 1 :
                pygame.quit()

        if (100 + 240) >= mouse[0] >= 100 and (350 + 40) >= mouse[1] >= 350 :
            
            if click[0] == 1 and loop == 0 :
                loop = 1
                dark_mode = not(dark_mode)

        if dark_mode == True :
            pygame.draw.circle(win, (0,0,0), (310, 370), 5, 0)
            pygame.draw.circle(win, (0,0,0), (140, 370), 5, 0)

        if (360 + 240) >= mouse[0] >= 360 and (350 + 40) >= mouse[1] >= 350 :
            
            if click[0] == 1 and loop2 == 0 :
                loop2 = 1
                game_music = not(game_music)

        if game_music == True :
            pygame.draw.circle(win, (0,0,0), (570, 370), 5, 0)
            pygame.draw.circle(win, (0,0,0), (400, 370), 5, 0)

        while (100 + 500) >= mouse[0] >= 100 and (450 + 40) >= mouse[1] >= 450 :
            
            if click[0] == 1 :
                about = pygame.image.load("about.png")
                s_about = pygame.transform.scale(about, (700,550))
                win.blit(s_about, (0,50))

            break


        pygame.display.update()
        win.fill(win_color)



    if dark_mode :
        gray = (205, 205, 205)

    else :
        gray = (50, 50, 50)

    color = gray
    clone_color = gray

    if game_music :
        pygame.mixer.music.play(-1)


# Final screen function :

def final_screen() :

    global score, final_score

    if score >= 10000 :
        final_score.play()

    if 9000 <= score <= 9950 :
        boo.play()

    over = True

    while over :

        pygame.time.delay(10)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        final_win = pygame.image.load("bg_8.png")
        s_fw = pygame.transform.scale(final_win, (700,650))

        color1 = (0,0,0)
        color2 = (255,255,255)

        if dark_mode == False :
            win.blit(s_fw,(0,0))

        if dark_mode :
            color1 = color2

        for event in pygame.event.get() :

            if event.type == pygame.QUIT :
                print("game over")
                pygame.quit()

        med_font = pygame.font.SysFont("Papyrus", 35)
        game_over = title_font.render("GAME OVER", True, color1)
        score_count = med_font.render("Score : " + str(score), True, color1)
        win.blit(game_over, (155,150))
        win.blit(score_count, (250, 250))

        if score >= 10000 :
            congrats = med_font.render("Congratulations my friend !", True, (255,0,0))
            congrats2 = med_font.render("you did it", True, (255,0,0))

            win.blit(congrats, (150,25))
            win.blit(congrats2, (280,75))

        if 9000 <= score <= 9950 :
            almostt = med_font.render("You almost did it", True, (255,0,0))
            win.blit(almostt, (220,75))

        button_1 = make_button(200,350,300,40, (325,360), "PLAY")
        button_2 = make_button(200,400,300,40, (310,410), "RETURN")
        button_3 = make_button(200,460,300,40, (325,470), "EXIT")

        if dark_mode == True :
            button_1 = make_dark_button(200,350,300,40, (325,360), "PLAY")
            button_2 = make_dark_button(200,400,300,40, (310,410), "RETURN")
            button_3 = make_dark_button(200,460,300,40, (325,470), "EXIT")

        if ((300+200) >= mouse[0] >= 200) and ((350+40) >= mouse[1] >= 350) :
            
            if click[0] == 1 :
                score = 0
                return shapes()

        if ((300+200) >= mouse[0] >= 200) and ((400+40) >= mouse[1] >= 400) :
            
            if click[0] == 1 :
                score = 0
                return intro_function()

        if ((300+200) >= mouse[0] >= 200) and ((460+40) >= mouse[1] >= 460) :
            
            if click[0] == 1 :
                score = 0
                pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] :
            score = 0
            return shapes()

        pygame.display.update()



# the main loop of the game :

intro_function()

if dark_mode :
    gray = (205, 205, 205)

else :
    gray = (50, 50, 50)

color = gray
clone_color = gray

run = True

while run :

    pygame.time.delay(10)

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :
            print("game over")
            run = False

    # left & right user's movement :

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and user_rect.x <= 700 - vel - width - 10 :
        user_rect.x += vel

    if keys[pygame.K_LEFT] and user_rect.x >= vel + 10 :
        user_rect.x -= vel

    # jumping with the space bar :  

    if not(isjump) :

        if keys[pygame.K_SPACE] :
            isjump = True
            
    else :
        
        if jumpcount >= -10 :
            neg = 1

            if jumpcount < 0 :
                neg = -1

            user_rect.y -= (jumpcount ** 2) * 0.25 * neg
            jumpcount -= 1

        else :

            isjump = False
            jumpcount = 10
            user_rect.y = 610


    win.fill(win_color)

    if dark_mode == True :
            win_color = (5, 5, 5)

    shapes()

    
pygame.quit()
