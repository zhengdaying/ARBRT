def isRepetitive(nlist:list):
    nSet=set(nlist)
    if len(nlist)>len(nSet):
        return True
    else:
        return False
list1=[1,2,1,3,1]
if isRepetitive(list1):
    print("have")
else:
    print("noting")
list2=['china','chinese']
if isRepetitive(list2):
    print("have")
else:
    print("nothing")

