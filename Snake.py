class Snake():
    xcor=300
    ycor=300
    head=[xcor,ycor]
    tail=[xcor-60,ycor]
    snake=[tail,[xcor-40,ycor],[xcor-20,ycor],head]
    def snakemovement(self,snakeD):
        if snakeD=="R":
            headprime=[self.head[0]+20,self.head[1]]
            self.snake.pop(0)
            self.snake.append(headprime)
            self.tail=self.snake[0]
            self.head=headprime
        if snakeD=="L":
            headprime = [self.head[0] - 20, self.head[1]]
            self.snake.pop(0)
            self.snake.append(headprime)
            self.tail = self.snake[0]
            self.head = headprime
        if snakeD == "U":
            headprime = [self.head[0], self.head[1]-20]
            self.snake.pop(0)
            self.snake.append(headprime)
            self.tail = self.snake[0]
            self.head = headprime
        if snakeD=="D":
            headprime = [self.head[0], self.head[1]+20]
            self.snake.pop(0)
            self.snake.append(headprime)
            self.tail = self.snake[0]
            self.head = headprime

    def snakegrow(self,snakeD):
        if snakeD=="R":
            headprime=[self.head[0]+20,self.head[1]]

            self.snake.append(headprime)

            self.head=headprime
        if snakeD=="L":
            headprime = [self.head[0] - 20, self.head[1]]

            self.snake.append(headprime)

            self.head = headprime
        if snakeD == "U":
            headprime = [self.head[0], self.head[1]-20]

            self.snake.append(headprime)

            self.head = headprime
        if snakeD=="D":
            headprime = [self.head[0], self.head[1]+20]

            self.snake.append(headprime)

            self.head = headprime
    def snake_collision(self):
        if self.head in self.snake[:-2]:
            return True
        elif (self.head[0]<0 or self.head[0]>580) or (self.head[1]<0 or self.head[1]>580):
            return True
        else:
            return False
