import random
x=random.randint(5000,10000)
change=0
nochange=0
for i in range(1,x+1):
    a=random.choice([1,2,3])
    b=random.choice([1,2,3])
    if a==b:
        nochange=nochange+1
    else:
        change=change+1
print("不更改选择后选中汽车的概率为{}".format(nochange/x))
print("更改选择后选中汽车的概率为{}".format(change/x))
