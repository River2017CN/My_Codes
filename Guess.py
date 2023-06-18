import random  # 导入random模
chance = 10  #回合次数限制
guess = 0

def isOK(num1,num2): # 定义函数
    global chance,guess
    if chance == 0:
        print("You have no more chances!")
        print("GAME OVER")
        exit()
    elif num1 < 0 or num1 > 100:
        print("Out of range. Please try again.")
        chance = chance - 1
        print("You have " + str(chance) + " chances left!")
        return False
    elif 0 < num1 < num2:
        print(guess + " is too small!")
        chance = chance - 1
        print("You have " + str(chance) + " chances left!")
        return False
    elif num1 > num2:
        print(guess + " is too big!")
        chance = chance - 1
        print("You have " + str(chance) + " chances left!")
        return False
    else:
        print("BINGO! It is " + guess + " !")
        return True

num = random.randint(1, 100)  # 在1到100之间取一个随机数

print("Guess which number am I thinking?(1-100)")
bingo = False

for i in range(chance):  #没必要，但万一，我是说万一，真的有人能突破限制呢？所以我设置了一个兜底措施（迫真）
    while not bingo and chance != 0:
        guess = input()
        try:
            answer = int(guess)
        except:
            print("Wrong input type. Try again.")
        bingo = isOK(answer,num)