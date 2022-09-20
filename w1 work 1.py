def is_prime(num):
  if (num<2):
    return False
  elif(num == 2):
    return True
  elif(num%2 == 0):
    return False
  i=2  
  while i<int(num/2):
    if(num%i == 0):
      return False
    i=i+1
  return True