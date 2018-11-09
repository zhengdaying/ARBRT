def isOdd(n):
    if n%2==1:
        return True
    else:
        return False
while True:
    s=input("请输入整数：")
    if not s.isdigit():
        print("请再次输入")
        continue
    n=eval(s)
    if n==1:
        print("结束")
        break
    if isOdd(n):
        print("{}是奇数".format(n))
    else:
        print("{}是偶数".format(n))
