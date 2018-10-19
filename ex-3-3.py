dayup,dayfactor=1.0,0.01
for i in range(1,365):
    if i%10 in [4,5,6,7]:
        dayup=dayup*(1+dayfactor)
    print("{}：天的能力{}".format(i+1,dayup))
    print("10天间断一天365天后的的能力为:{:.2f}".format(dayup))
dayup,dayfactor=1.0,0.01
for i in range(1,365):
    if i%15 in [4,5,6,7,14,15,16,17]:
        dayup=dayup*(1+dayfactor)
    print("{}：天的能力{}".format(i+1,dayup))
    print("15天间断一天365天后的的能力为:{:.2f}".format(dayup))
