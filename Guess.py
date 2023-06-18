import random  # 导入random模
chance = 10  #回合次数限制
guess = ""

def isOK(num1,num2): # 定义函数
    global chance,guess  #程序怎么run了？把这去掉试试！
    if num1 < 0 or num1 > 100:
        print("Out of range. Please try again.")
    elif 0 < num1 < num2:
        print(guess + " is too small!")
    elif num1 > num2:
        print(guess + " is too big!")
    else:
        print("BINGO! It is " + guess + " !")
        return True
    chance -= 1
    print("You have " + str(chance) + " chances left!")
    return False

num = random.randint(1, 100)  # 在1到100之间取一个随机数

print("Guess which number am I thinking?(1-100)")
bingo = False

while not bingo:
    if chance == 0:
        print("You have no more chances!")
        print("The answer is " + str(num) + " !")
        print("GAME OVER")
        bingo = True
        break
    guess = input()
    try:
        answer = int(guess)
    except:
        print("Wrong input type. Try again.")
    bingo = isOK(answer,num)