k = int(input("enter the number: "))
i = 2
while(i < k):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " is prime")
   i = i + 1

print ("Good bye!")

#Explanation: This code checks if a number is prime by iterating from 2 to the square root of the number. 
# If the number is divisible by any number in this range, it is not prime. Otherwise, it is prime. The loop continues until the number is checked, and the prime numbers are printed. 
# The code also handles the case where the input number is 1, as 1 is not considered prime. The loop terminates when the square root of the number
