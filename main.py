import pygame
import random
import time



# initialise game
pygame.init()

# game window size
WIDTH, HEIGHT = 400, 400
GAME_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Gen")

# initialise snake
x, y = 200, 200
# distance snake can move
snake_x, snake_y = 10, 0

# food initialisation
food_x, food_y = random.randrange(0, WIDTH)//10*10, random.randrange(0, HEIGHT)//10*10 

# initialise length of snake
body_list = [(x, y)]

# slow down the for loop to reduce snake speed
FRAME_RATE = pygame.time.Clock()

game_over = False

font = pygame.font.SysFont("bahnschrift", 25)

# create snake
def snake():
  # initialised outside function, made global
  global x, y, food_x, food_y, game_over

  # location of snake, stay within screen area
  x = (x + snake_x) % WIDTH
  y = (y + snake_y) % HEIGHT

  # game over if contact with itself
  if ((x, y) in body_list):
    game_over = True
    return
  
  body_list.append((x, y))

  # if snake eats or does not
  if (food_x == x and food_y == y):
    while((food_x, food_y) in body_list):
      food_x, food_y = random.randrange(0, WIDTH)//10*10, random.randrange(0, HEIGHT)//10*10 
  else:
    del body_list[0]

  # clear screen on snake movement
  GAME_SCREEN.fill((0, 0, 0))
  # player score
  score = font.render("Score: " + str(len(body_list)), True, (255, 255, 0))
  GAME_SCREEN.blit(score, [0, 0])
  # create food on screen
  pygame.draw.rect(GAME_SCREEN, (255, 0, 0), [food_x, food_y, 10, 10])
  # increase length of snake
  for (i, j) in body_list:
    # create snake on screen
    pygame.draw.rect(GAME_SCREEN, (255, 255, 255), [i, j, 10, 10])
  pygame.display.update()
  

# keep game window alive
while True:
  if (game_over):
    GAME_SCREEN.fill((0, 0, 0))
    score = font.render("Score: " + str(len(body_list)), True, (255, 255, 0))
    GAME_SCREEN.blit(score, [0, 0])
    msg = font.render("GAME OVER!", True, (255, 255, 255))
    GAME_SCREEN.blit(msg, [WIDTH//3, HEIGHT//3])
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()
  # check events, find closing window event
  events = pygame.event.get()
  for event in events:
    if (event.type == pygame.QUIT):
      # quit game
      pygame.quit()
      quit()
    # snake movement via keyboard
    if (event.type == pygame.KEYDOWN):
      # move left, not y
      if (event.key == pygame.K_LEFT):
        if (snake_x != 10):
          snake_x = -10
        snake_y = 0
      # move right, not y
      elif (event.key == pygame.K_RIGHT):
        if (snake_x != -10):
          snake_x = 10
        snake_y = 0
      # move up, not x
      elif (event.key == pygame.K_UP):
        snake_x = 0
        if (snake_y != 10):
          snake_y = -10
      # move down, not x
      elif (event.key == pygame.K_DOWN):
        snake_x = 0
        if (snake_y != -10):
          snake_y = 10
      # anyother key pressed, do nothing
      else:
        continue
      snake()
  # continuous scroll from snake    
  if(not events):
    snake()
  # reduce snake frame rate / speed of snake
  FRAME_RATE.tick(10)   

