import  random
def generatePSW(n:int, chList:list):
    psw=[]
    size=len(chList)
    for i in range(n):
      k=random.randint(0,size-1)
      psw.append(chList[k])
    return "".join(psw)
chs=[]
c='A'
while c<='Z':
    chs.append(c)
    c=chr(ord(c)+1)
c='a'
while c<='z':
    chs.append(c)
    c=chr(ord(c)+1)
c='1'
while c<='9':
    chs.append(c)
    c=chr(ord(c)+1)
pswlist=[]
for i in range(10):
    print("第{0:2}个随机密码:{1}".format(i+1,generatePSW(8,chs)))
