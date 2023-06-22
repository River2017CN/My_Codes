import random

class Guess:
    def __init__(self) -> None:
        self.target = random.randint(0, 100)
        self.tries = 10
        self.end = False

    def answer(self, ans: int):
        if self.end:
            print("游戏已经结束啦！")
            return
        if ans > self.target:
            print("太大了，不行！")
        elif ans < self.target:
            print("小幼女喵")
        else:
            print("你猜对啦")
            self.end = True
            return
        self.tries -= 1
        if self.tries <= 0:
            print(f"你没有机会啦。正确答案是{self.target}")
            self.end = True

game = Guess()
while not game.end:
    game.answer(int(input("输入数字: ")))
