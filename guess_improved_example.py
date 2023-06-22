import random

class Guess:
    def __init__(self, tries, r) -> None:
        self.target = random.randint(0, r)
        self.tries = tries
        self.end = False

    def chance_str(self):
        if self.tries <= 1:
            return ""
        else:
            return f"你还有{self.tries - 1}次机会..."
    def answer(self, ans: int):
        if self.end:
            print("游戏已经结束啦！")
            return
        if ans > self.target:
            print(f"太大了，不行！{self.chance_str()}")
        elif ans < self.target:
            print(f"小幼女喵~ {self.chance_str()}")
        else:
            print("你猜对啦")
            self.end = True
            return
        self.tries -= 1
        if self.tries <= 0:
            print(f"你没有机会啦。正确答案是{self.target}")
            self.end = True

played = False

def inp_int(p: str) -> int:
    r = 0
    while True:
        try:
            r = int(input(p))
            break
        except KeyboardInterrupt:
            raise KeyboardInterrupt("输入中断啦，直接退出啦")
        except:
            print("输入有误啦，再试一次~")
    return r

def inp_m(p: str, _min: int, _max: int) -> int:
    while True:
        r = inp_int(p)
        if r > _max:
            print(f"太大了，不行！最大数字是{_max}哦")
            continue
        if r < _min:
            print(f"小幼女喵！最小数字是{_min}喵")
            continue
        return r

while True:
    print(f"这位客官{'还要再来一次' if played else '要玩玩猜数游戏'}嘛")
    玩游戏嘛 = input("输入[来]还是[不来]" if played else "输入[玩]还是[不玩]:")
    if (not played and 玩游戏嘛 != "玩") or (played and 玩游戏嘛 != "来"):
        break
    r = inp_m("现在输入数字范围啦: 0 - ", 10, 200)
    m = inp_m("你有多大胜算呢？输入最大尝试次数吧: ", 3, 10)
    game = Guess(m, r)
    while not game.end:
        game.answer(inp_m("输入数字: ", 0, r))
    played = True
