o=input("请输入一行字符：")
alphabet=0
number=0
space=0
other=0
for c in o:
    if 'A'<=c<='Z'or'a'<=c<='z':
        alphabet+=1
    elif '0'<=c<='9':
        number+=1
    elif c.isspace():
        space+=1
    else:
        other+=1
print("此行有{}个字母，{}个数字，{}个空格，{}个其他字符".format(alphabet,number,space,other))
