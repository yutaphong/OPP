def convertToBinary(n):
   #Function: print binary number for the input decimal using recursion
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 246

#convert
convertToBinary(dec)