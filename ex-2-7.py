from turtle import*
seth(30)
while True:
    fd(90)
    left(120)
    if abs(pos())<1:
        break
seth(90)
fd(45)
left(90)
pu()
fd(1.73*15)
pd()
seth(-30)
for i in range(3):
    fd(90)
    left(120)
