def fab(n):
  if n==1:
      return 1
  if n==0:
      return 0
  else:
      result=int(fab(n-1))+int(fab(n-2))
      return result
for i in range(11):
  print ("菲波那锲递归为{0:}".format(fab(i)))
