from random import*
seed(0)
t=randint(0,100)
count=0
while True:
    n=eval(input("请输入一个0到100之间的整数:"))
    count+=1
    if n>t:
        print("遗憾太大了")
    elif n==t:
        print("预测了{}次，你猜中了".format(count))
    else:
        print("遗憾太小了")
