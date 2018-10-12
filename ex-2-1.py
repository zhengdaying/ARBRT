SymbolStr=input("请输入温度体系符号：")
if SymbolStr in['f','F']:
    t=eval(input("请输入温度值："))
    C=int((t-32)/1.8)
    print("转换后的温度是：{}C)".format(C))
elif SymbolStr in['C','c']:
    t=eval(input("请输入温度值："))
    F=int(t*1.8+32)
    print("转换后的温度值是：{}F".format(F))
else:
    print("输入符号错误")
    
