import random_number
import check_number

#乱数生成＆入力
def choose_or_random():
    command=input('choose or random ')
    if command=="choose":
        random_number.generate_number_choose()
    elif command=="random":
        random_number.generate_number_random()
    else:
        print("please answer 'choose' or 'random'")
        choose_or_random()
choose_or_random()

#判定プログラム
check_number.check_and_count(random_number.guess,random_number.answer)
