SymbolStr=input("请输入货币体系符号：")
#美元用“D”，“d”人民币用“R”，“r”
if SymbolStr in['R','r']:
    t=eval(input("请输入货币值："))
    D=t/6
    print("转换后的货币是：{}D)".format(D))
elif SymbolStr in['D','d']:
    t=eval(input("请输入货币值："))
    R=int(t*6)
    print("转换后的货币值是：{}R".format(R))
else:
    print("输入符号错误")
    
