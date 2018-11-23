def isPrime(n):
    for i in range(2,n):
        if n%1==0:
            return False
        return True
while True:
    try:
        n=eval(input("输入一个整数："))
    except:
        print("请再次输入：")
        continue
    if type(n) is not int:
        print("请输入1个整数：")
        continue
    if n==-1:
        break
    if isPrime(n):
        print("{} is prime".format(n))
    else:
        print("{} is not prime".format(n))
