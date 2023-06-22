import random  # 导入random模
chance = 10  #回合次数限制
guessed = ""

def verify(player_answer:int,really_answer:int): # 定义函数
    """Is player's answer match?"""
    global chance,guessed  #程序怎么run了？把这去掉试试！
    if player_answer < 0 or player_answer > 100:
        print("Out of range. Please try again.")
    elif 0 < player_answer < really_answer:
        print(guessed + " is too small!")
    elif player_answer > really_answer:
        print(guessed + " is too big!")
    else:
        print("BINGO! It is " + guessed + " !")
        return True
    chance -= 1
    print("You have " + str(chance) + " chances left!")
    return False

'''
def isFUCK(fak):  #无意义函数，但是我真的写了！
    """Fuck you"""
    global chance,guess
    match fak:
        case num:
            return True
'''

r_answer = random.randint(1, 100)  # 在1到100之间取一个随机数

print("Guess which number am I thinking?(1-100)")
bingo = False


while not bingo:
    if chance == 0:
        print("You have no more chances!")
        print("The answer is " + str(r_answer) + " !")
        print("GAME OVER")
        bingo = True
        break

    guessed = input("Your answer:")
    allowed = False

    try:
        p_answer = int(guessed)
        allowed = True
    except:
        print("Wrong input type. Try again.")
    if allowed:
        bingo = verify(p_answer,r_answer)
    else:
        chance -= 1
