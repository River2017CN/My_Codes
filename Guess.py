import random  # 导入random模块

def isOK(num1,num2): # 定义函数
    if num1 < 0 or num1 > 100:
        print("Out of range. Please try again.")
    elif 0 < num1 < num2:
        print(guess + " is too small!")
        return False;
    elif num1 > num2:
        print(guess + " is too big!")
        return False;
    else:
        print("BINGO! It is " + guess + " ！")
        return True

num = random.randint(1, 100)  # 在1到100之间取一个随机数

print("Guess which number am I thinking?(1-100)")
bingo = False

while not bingo:
    guess = input()
    try:
        answer = int(guess)
        bingo = isOK(answer,num)
    except:
        print("Wrong input type. GAME OVER.")
        exit()
