import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

#create icon
pygame_icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("Rock - Paper - Scissors")

#load font & color
font = pygame.font.SysFont('consolas', 20)
font2 = pygame.font.SysFont('consolas', 15)
font3 = pygame.font.SysFont('freesanbold', 23)
vsfont = pygame.font.SysFont('freesanbold', 40)
screencolor = (240, 240, 240)
black = (0, 0, 0)
white = (255, 255, 255)
gray1 = (204, 204, 204)
gray2 = (190, 190, 190)

#create screen
screen = pygame.display.set_mode((315, 360))

#load sounds
win_sound = pygame.mixer.Sound('sounds/win_sound.wav')
lose_sound = pygame.mixer.Sound('sounds/game_over_sound.wav')
draw_sound = pygame.mixer.Sound('sounds/draw_sound.wav')

#load images and button images
scissors = pygame.image.load('images/scissors.png')
rock = pygame.image.load('images/rock.png')
paper = pygame.image.load('images/paper.png')
blur = pygame.image.load('images/blur.png')

scissors_button = pygame.image.load('images/scissors_button.png')
rock_button = pygame.image.load('images/rock_button.png')
paper_button = pygame.image.load('images/paper_button.png')

#make a function that create buttons
def createbuttons():
    screen.blit(rock_button, (30, 270))  
    screen.blit(paper_button, (120, 270))
    screen.blit(scissors_button, (210, 270))  

running = True
while True:
    while running:
        #reset variables
        player = ""
        winning = ""
        playerchoose = False
        bot = None

        screen.fill(screencolor)

        #make title on the screen
        title = font.render("Rock - Paper - Scissors", True, black)
        titleRect = title.get_rect()
        titleRect.center = (160, 50)
        screen.blit(title, titleRect)
        
        createbuttons()

        #check if the mouse is clicked to the box
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            mouse = pygame.mouse.get_pos()
            if 30 <= mouse[0] <= 90 and 270 <= mouse[1] <=310 and event.type == pygame.MOUSEBUTTONDOWN:
                player = "rock"
                playerchoose = True
            elif 120 <= mouse[0] <= 180 and 270 <= mouse[1] <=310 and event.type == pygame.MOUSEBUTTONDOWN:
                player = "paper"
                playerchoose = True
            elif 210 <= mouse[0] <= 270 and 270 <= mouse[1] <=310 and event.type == pygame.MOUSEBUTTONDOWN:
                player = "scissors"
                playerchoose = True

        #create computer's choice       
        if playerchoose:
            bot = random.choice(["rock", "paper", "scissors"])
            vs_txt = vsfont.render("VS", True, black)
            vsRect = vs_txt.get_rect()
            vsRect.center = (160, 135)
            screen.blit(vs_txt, vsRect)

        #check winning conditions
        if player == "rock":
            if bot == "paper":
                winning = False
                screen.blit(rock, (50, 100))
                screen.blit(paper, (215, 100))
            if bot == "scissors":
                winning = True
                screen.blit(rock, (50, 100))
                screen.blit(scissors, (215, 100))
            if bot == "rock":
                winning = None
                screen.blit(rock, (50, 100))
                screen.blit(rock, (215, 100))
            pygame.display.update()

        elif player == "scissors":
            if bot == "paper":
                winning = True
                screen.blit(scissors, (50, 100))
                screen.blit(paper, (215, 100))
            if bot == "scissors":
                winning = None
                screen.blit(scissors, (50, 100))
                screen.blit(scissors, (215, 100))
            if bot == "rock":
                winning = False
                screen.blit(scissors, (50, 100))
                screen.blit(rock, (215, 100))
            pygame.display.update()

        elif player == "paper":
            if bot == "paper":
                winning = None
                screen.blit(paper, (50, 100))
                screen.blit(paper, (215, 100))
            if bot == "rock":
                winning = True
                screen.blit(paper, (50, 100))
                screen.blit(rock, (215, 100))
            if bot == "scissors":
                winning = False
                screen.blit(paper, (50, 100))
                screen.blit(scissors, (215, 100))
            pygame.display.update()

        #print to the screen
        if winning == True:
            msg = font.render("You win!", True, black)
            msgRect = msg.get_rect()
            msgRect.center = (160, 190)
            screen.blit(msg, msgRect)
            pygame.display.update()
            running = False
            win_sound.play()

        elif winning == False:
            msg = font.render("You lose!", True, black)
            msgRect = msg.get_rect()
            msgRect.center = (160, 190)
            screen.blit(msg, msgRect)
            pygame.display.update()
            running = False
            lose_sound.play()

        elif winning == None:
            msg = font.render("Draw!", True, black)
            msgRect = msg.get_rect()
            msgRect.center = (160, 190)
            screen.blit(msg, msgRect)
            pygame.display.update()
            running = False
            draw_sound.play()

        pygame.display.update()
    
    #create TRY AGAIN button
    while not running:
        screen.blit(blur, (30, 270))
        #pygame.draw.rect(screen, screencolor, pygame.Rect(30, 220, 360, 150))

        button = pygame.draw.rect(screen, gray1, (90, 220, 140, 30))
        button_ = pygame.draw.rect(screen, black, (90, 220, 140, 30), 2)
        try_again_text = font.render("Try again", True, black)
        try_again_textRect = try_again_text.get_rect()
        try_again_textRect.center = (160, 235)

        screen.blit(try_again_text, try_again_textRect)

        mouse = pygame.mouse.get_pos()
        if 90 <= mouse[0] <= 230 and 220 <= mouse[1] <= 250:
            button = pygame.draw.rect(screen, gray2, (90, 220, 140, 30))
            button_ = pygame.draw.rect(screen, black, (90, 220, 140, 30), 2)
            screen.blit(try_again_text, try_again_textRect)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = True

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()