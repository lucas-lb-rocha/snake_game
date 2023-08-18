from random import randint

class Apple:
    
    def __init__(self) -> None:
        self.x = randint(40, 600)
        self.y = randint(50, 430)
    
    def updateXandY(self) -> None:
        self.x = randint(40, 600)
        self.y = randint(50, 430)