import random
from typing import Self
class Guess:
    def __init__(self):
        print("Guess which number am I thinking about?(0-100)")
        RAnswer = random.randint(0,100)
        self.ranswer = RAnswer
        self.chances = 10
        self.bingo = False
        return
    def capture(self,inside):
        try:
            PlA = int(inside)
            self.verify(PlA)
        except:
            print("Type error,I will make a choice for you carefully.")
            CmA = random.randint(1,100)
            if CmA == self.ranswer:
                CmA = random.randint(1,100)
            self.verify(CmA)
    def verify(self,Player_answer:int):
        if self.chances <= 0:
            print(f"GAME OVER! The answer is {self.ranswer}!")
            self.bingo = True
        elif Player_answer > 100 or Player_answer < 0:
            self.chances -= 1
            print(f"{Player_answerr} is out of range. Please try again.")
            print(f"You have {self.chances} times left!")
        elif Player_answer > self.ranswer:
            self.chances -= 1
            print(f"{Player_answer} is too big!")
            print(f"You have {self.chances} times left!")
        elif Player_answer < self.ranswer:
            self.chances -= 1
            print(f"{Player_answer} is too small!")
            print(f"You have {self.chances} times left!")
        else:
            print(f"Yes,it is {Player_answer}!")
            self.bingo = True

aaa = Guess()
while not aaa.bingo:
    aaa.capture(input("Your answer:"))