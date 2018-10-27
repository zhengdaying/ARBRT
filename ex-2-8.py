from turtle import*
edge=5
setup(500,500,200,200)
pu()
while edge<200:
    theta=0
    fd(edge)
    theta=theta+90
    pd()
    seth(theta)
    fd(edge)
    theta=theta+90
    seth(theta)
    edge=edge+5
    fd(edge)
    theta=theta+90
    seth(theta)
    theta=theta+90
    fd(edge)
    seth(theta)
    edge=edge+5


