import random

class Food():
    xcor= random.randint(1,29)*20
    ycor= random.randint(1,29)*20
    food=[xcor,ycor]

    def generatefood(self):

        self.xcor = random.randint(1, 29)*20
        self.ycor = random.randint(1, 29)*20
        self.food=[self.xcor,self.ycor]
        return self.food

    def check_food_generation(self,snakebody):
        self.food=self.generatefood()
        if self.food in snakebody:
            self.generatefood()
        else:
            return self.food

