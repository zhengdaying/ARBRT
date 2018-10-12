from turtle import*
while True:
    fd(120)
    left(120)
    if abs(pos())<1:
        break
fd(60)
left(60)
for i in range(3):
    fd(60)
    left(120)
seth(120)
fd(60)
seth(0)
