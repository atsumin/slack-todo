import random
words=['slack','python','root','clock','environment','pencil','hangman','twitter','vacation','vaccine','quality','excellent',
       'justice','ax','boy','github','panda','kangaroo','bamboo','pentagon','freedom','communication','quater','weekend',
       'fake','champion','queen','elephant','typhoon','children','cherry','chapsticks','carbondioxide','kingdom','prestige',
       'fireworks','doctor','chemistry','mouse','genius','chocolate','ambitious','history','dinasour','vanilla',
       'mathematics','newton','halloween','physics','rhythm','gorilla','taxi','xylophone','tower','balloon']
def random_word():
    global guess
    global answer
    answer=words[random.randint(0,len(words)-1)]
    fuga="*"*(len(answer))
    print(fuga)
    guess=input("What's your guess?")


#ワード数表示（完成したらなくす）
print("There are "+str(len(words))+" words in the list.")
                
