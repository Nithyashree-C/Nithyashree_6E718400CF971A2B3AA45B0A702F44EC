#1.2 Program to find whether userdefined year a leap year/not by if-elif-else statements.

def isLeap(yr):
  if (yr % 4 == 0 and yr % 100 != 0):
    return True
  elif (yr % 400 == 0):
    return True
  else:
    return False

yr = int(input("\nEnter Year : "))

if isLeap(yr):
  print("\n{} is a Leap year.\n".format(yr))
else:
  print("\n{} is not a Leap year.\n".format(yr))
  
