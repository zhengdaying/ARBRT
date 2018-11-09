def isNum(s):
    try:
        n=eval(s)
    except:
        return False
    return True
s=input("请输入一个字符串：")
if isNum(s):
    print("{}属于".format(s))
else:
    print("{}不属于".format(s))
    
