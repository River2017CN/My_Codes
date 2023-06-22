'''
A program to learn "class". Taught by @sb-child.
❗Warning:NSFW
'''
# first,let's created a little sb-child!
import random
from typing import Self
class Sbchild:
    def __init__(self,Name):
        Pronoun = random.choice(["It","She"])
        print(f"Sb-child has had a baby! {Pronoun}'s a little sb-child called {Name}!")
        self.how_many_times = 0
        self.name = Name
        self.pronoun = Pronoun
        return
# if don't do below things,she won't do anything!
    def play_boobs(self):
        if self.pronoun == "It":
            print(f"{self.name}:Awwwww...")  # 真刑啊真可铐啊，虽然我很想用英语但我必须得用中文狠狠表扬这么出生的行为（大雾
            return
        if self.how_many_times < 5:
            print(f"{self.name}:Oh,I feel something amazing!")
        elif self.how_many_times < 10:
            print(f"{self.name}:Nya~I feel amazing...")
        elif self.how_many_times < 30:
            print(f"{self.name}:Nya~~~Don't stop that!!!")
        else:
            print(f"{self.name}:Feels good~Let's hug~")
        self.how_many_times += 1
    def hug(self,Another_sbchild:Self):
        print(f"[System]{self.name} has hugged {Another_sbchild.name} !")
class You:
    def __init__(self,Name):
        self.hname = Name
    def sex(self,The_first_sbchild:Sbchild,The_second_sbchild:Sbchild):
        print(f"[System]{self.hname} has sexed with {The_first_sbchild.name} & {The_second_sbchild.name}!")

# make her be a variable,or she will die!
sb_child_1 = Sbchild("Little sb-child younger")
sb_child_2 = Sbchild("Little sb-child elder")  # you are a HENTAI so you can play 2 little sb-children at the same time
Hentai = You(input("Enter your name,hentai:"))
for i in range(40):
    Sbchild.play_boobs(sb_child_1)
    sb_child_2.play_boobs()  # ok you hentai
sb_child_1.hug(sb_child_2)
Hentai.sex(sb_child_1,sb_child_2)


"""
写完了，已自首，喜提枪毙十八遍，大家下辈子再见
"""