dayup,dayfactor=1.0,0.01
for i in range(365):
    if i% 7 not in [3,4,5,6]:
        dayup=dayup*(dayfactor+1)
print("七天间断一天365天后的的能力为：{:.2f}".format(dayup))
