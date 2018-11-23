def hanoi(a,b,c,p):
    if len(p) == 1:
        print("圆盘{}:{}-->{}".format( str(p[0]), a, c))
    else:
        hanoi(a,c,b,p[0:-1])
        hanoi(a,b,c,[p[-1]])
        hanoi(b,a,c,p[0:-1])
p=["1","2","3","4",]
hanoi('a','b','c',p)
