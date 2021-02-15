

import pygame 
import random 

# Initializes pygame

pygame.init()

# width and a height of screen

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # creates the screen and gives it the width and height 

# creates the player and gives it the image found 

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
monster_enemy2 = pygame.image.load("monster.jpg")
drego_enemy3 = pygame.image.load("drego.jpg")
prize = pygame.image.load("prize.jpg")

#height and width of the images

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
monster_enemy2_height = monster_enemy2.get_height()
monster_enemy2_width = monster_enemy2.get_width()
drego_enemy3_height = drego_enemy3.get_height()
drego_enemy3_width = drego_enemy3.get_width()
prize_width = prize.get_width()
prize_height = prize.get_height()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))
 

playerXPosition = 100
playerYPosition = 50

# Makes the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

monster_enemy2XPosition = screen_width
monster_enemy2YPosition = random.randint(0, screen_height-monster_enemy2_height)

drego_enemy3XPosition = screen_width
drego_enemy3Yposition = random.randint(0, screen_height - drego_enemy3_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

#checks if the up or down key is pressed.

keyUp= False
keyDown = False
keyRight = False
keyLeft = False

# the game loop
# represent real time game play. 

while 1:  

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(monster_enemy2, (monster_enemy2XPosition, monster_enemy2YPosition))
    screen.blit(drego_enemy3, (drego_enemy3XPosition,drego_enemy3Yposition))
    screen.blit(prize, (prizeXPosition,prizeYPosition))

    pygame.display.flip()# This updates the screen. 
    
    #  loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False


    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    
    if keyLeft == True:
        if playerXPosition > 0 :
            playerXPosition -= 1
    if keyRight == True :
        if playerXPosition < screen_width - image_height:
            playerXPosition += 1 
    
    # Checks for collision of the enemy with the player.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    
    monster_enemy2Box = pygame.Rect(monster_enemy2.get_rect())
    monster_enemy2Box.top = monster_enemy2YPosition
    monster_enemy2Box.left = monster_enemy2XPosition

    drego_enemy3Box = pygame.Rect(drego_enemy3.get_rect())
    drego_enemy3Box.top = drego_enemy3Yposition
    drego_enemy3Box.left = drego_enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
   # Test collision of the boxes:

    
    if playerBox.colliderect(enemyBox):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
        
        
    if playerBox.colliderect(monster_enemy2Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit(0)
            
    if playerBox.colliderect(drego_enemy3Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

        # Display losing status to the user:


    if playerBox.colliderect(prizeBox):
        print("You win!")
       
        # Quite game and exit window: 
        pygame.quit()
        exit(0)
    
 
    
    #enemy approaches the player.
    
    enemyXPosition -= 0.15
    monster_enemy2XPosition -= 0.20
    drego_enemy3XPosition   -= 0.18
    prizeXPosition -= 0.17
    
