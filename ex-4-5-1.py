from random import*
seed(0)
t=randint(0,100)
count=0
while True:
    try:
        n=int(input("输入一个0-100数字:"))
    except:
        print("输入错误，请再输入！")
        continue
    count+=1
    if n>t:
        print("遗憾太大了")
    elif n==t:
        print("预测了{}次，你猜中了".format(count))
    else:
        print("遗憾太小了")
