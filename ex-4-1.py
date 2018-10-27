p=7
count=0
while True:
    n=eval(input("请输入一个0到9之间的整数:"))
    count+=1
    if n>p:
        print("遗憾太大了")
    elif n<p:
        print("遗憾太小了")
    else:
        print("预测了{}次，你猜中了".format(count))
        break
