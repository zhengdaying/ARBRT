a,b=eval(input("请输入两个整数，中间用逗号隔开："))
if a<b:
    m,n=b,a
else:
    m,n=a,b
r=m%n
while r!=0:
    m,n=n,r
    r=m%n
print("{}和{}最大约数是:{},最小公倍数是:{}".format(a,b,n,a*b/n))
