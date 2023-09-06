#1.1 Implement a recursive function to calculate the factorial of a given number.

def fact(n):
  if (n==0 or n==1):
    return 1
  else:
    return n*fact(n-1)

num = 2
result = fact(num)

print("\nThe factorial of {} is {}. ".format(num,result))


