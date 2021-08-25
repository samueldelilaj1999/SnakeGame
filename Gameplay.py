import pygame
from Snake import Snake
from Food import Food
class Gameplay():
    width=600
    height=600
    dimensions=(width,height)
    screen=pygame.display.set_mode(dimensions)
    pygame.display.set_caption("SnakeGame")
    snakeD="R"
    snake=Snake()
    snakebody=snake.snake
    food=Food()
    newfood=food.food
    gameon=True
    gameover=False
    score=0
    
    with open("highscore.txt") as file:
        highscore=int(file.read())


    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 60)
    myfont1 = pygame.font.SysFont('Comic Sans MS', 20)


    def  __init__(self,snakespeed,bgcolor,snakecolor):
        self.snakespeed=snakespeed
        self.bgcolor=bgcolor
        self.snakecolor=snakecolor
        self.showscreen()
    def draw_components(self):
        #draw grid
        for i in range(0,int(self.width/20)):
            pygame.draw.line(self.screen,(0,0,0),(0,i*20),(self.width,i*20))
            pygame.draw.line(self.screen,(0,0,0),(i*20,0),(i*20,self.width))
        #draw snake
        for i in self.snakebody:
            if i==self.snake.head:
                pygame.draw.rect(self.screen, (200,0,0), pygame.Rect(i[0], i[1], 20, 20))
            else:
                pygame.draw.rect(self.screen,self.snakecolor,pygame.Rect(i[0],i[1],20,20))
        pygame.draw.rect(self.screen,(0,100,100),pygame.Rect(self.newfood[0],self.newfood[1],20,20))
    def snake_eat(self):

        if self.snake.head==self.newfood:
            self.score+=1
            self.snakespeed+=120
            self.snake.snakegrow(self.snakeD)
            self.newfood=self.food.check_food_generation(self.snakebody)
    def input_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameon = False
            # KEYBOARD INPUT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and (self.snakeD == "R" or self.snakeD == "L"):
                    self.snakeD = "D"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and (self.snakeD == "R" or self.snakeD == "L"):
                    self.snakeD = "U"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and (self.snakeD == "U" or self.snakeD == "D"):
                    self.snakeD = "R"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and (self.snakeD == "U" or self.snakeD == "D"):
                    self.snakeD = "L"
    def showscreen(self):
        while self.gameon:
            self.screen.fill(self.bgcolor)
            self.draw_components()
            self.input_manager()
            if self.gameover==True:
                pygame.time.wait(2000)
                self.gameon=False
            self.snake.snakemovement(self.snakeD)
            self.snake_eat()
            self.gameover=self.snake.snake_collision()
            if self.gameover==True:
                textsurface = self.myfont.render('GAME OVER',False, (0,0,0))
                self.screen.blit(textsurface, (120,250))
            textsurface1 = self.myfont1.render(f"Score:{self.score}", False, (0, 0, 0))
            self.screen.blit(textsurface1, (10, 10))
            if self.score>=self.highscore:
                self.highscore=self.score
                with open("highscore.txt",mode="w") as file:
                    file.write(str(self.highscore))

            textsurface12 = self.myfont1.render(f"HighScore:{self.highscore}", False, (0, 0, 0))
            self.screen.blit(textsurface12, (100, 10))
            timedelay=int((10000-self.snakespeed)/30)
            pygame.display.flip()
            pygame.time.delay(timedelay)
