#Game Definitions...

import pygame, sys, random
from pygame.math import Vector2

pygame.init()

titleFont = pygame.font.Font(None, 25)
scoreFont = pygame.font.Font(None,35)

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cellSize = 20
numOfCells = 20

OFFSET = 60

# Creating the food...
class Food:
    def __init__(self, snakeBody):
        self.position = self.generate_random_position(snakeBody)

    def draw(self):
        food_rect = pygame.Rect(OFFSET + self.position.x*cellSize, OFFSET + self.position.y*cellSize, cellSize, cellSize)
        pygame.draw.rect(screen, DARK_GREEN, food_rect)

    def generate_random_cell(self):
        x = random.randint(0, numOfCells-1)   # Generates random positions btwn 0 and 19 because we have 20 cells
        y = random.randint(0, numOfCells-1)   
        return Vector2(x, y)

    def generate_random_position(self, snakeBody):
        position = self.generate_random_cell()
        while position in snakeBody:
            position = self.generate_random_cell()
        return position
       
    
# Creating the snake...
class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1, 0)
        self.addSegment = False

    def draw(self):
        for segment in self.body:
            segment_rect = (OFFSET + segment.x*cellSize, OFFSET + segment.y*cellSize, cellSize, cellSize)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction) 
        if self.addSegment == True:
            self.addSegment = False
        else:
            self.body = self.body[:-1] # Selects all elements from the beginning of the list upto the 2nd last element

    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1, 0)

            


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"
        self.score = 0

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.checkCollisionWithFood()
            self.checkCollisionWithEdges()
            self.checkCollisionWithBody()

    def checkCollisionWithFood(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_position(self.snake.body)
            self.snake.addSegment = True
            self.score += 1

    def checkCollisionWithEdges(self):
        if self.snake.body[0].x == numOfCells or self.snake.body[0].x == -1:
            self.gameOver()
        if self.snake.body[0].y == numOfCells or self.snake.body[0].y == -1:
            self.gameOver()

    def gameOver(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_position(self.snake.body)
        self.state = "STOPPED"
        self.score = 0

    def checkCollisionWithBody(self):
        headlessBody = self.snake.body[1:]
        if self.snake.body[0] in headlessBody:
            self.gameOver()
        
        
        

screen = pygame.display.set_mode((2*OFFSET + cellSize*numOfCells, 2*OFFSET + cellSize*numOfCells))  

pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock() #Controls the gamespeed

game = Game()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
           
        if event.type == pygame.KEYDOWN: # This line checks whether the user has pressed a key
            if game.state == "STOPPED":
                game.state = "RUNNING"
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0,1):
                game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0,-1):
                game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1,0):
                game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1,0):
                game.snake.direction = Vector2(-1,0)

    # Drawing
    screen.fill(GREEN) # This line fills the screen with our desired colour
    pygame.draw.rect(screen, DARK_GREEN, (OFFSET-5, OFFSET-5, cellSize*numOfCells + 10, cellSize*numOfCells + 10), 5)
    game.draw()

    titleSurface = titleFont.render("Retro Snake", True, DARK_GREEN)
    scoreSurface = scoreFont.render(str(game.score), True, DARK_GREEN)
    screen.blit(titleSurface, (OFFSET-5, 20))
    screen.blit(scoreSurface,(OFFSET-5, OFFSET +cellSize*numOfCells + 10))

    pygame.display.update()
    clock.tick(60)



