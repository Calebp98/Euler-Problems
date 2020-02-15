num = 2520
upper = 20
nUpper = upper
condition =0

while(condition==0):
  if(nUpper==0):
    condition = 1
    print("passed")
    print(num)
  else:  
    if(num%nUpper==0):
      nUpper =nUpper-1
    else:
      num = num+2520
      nUpper = upper
