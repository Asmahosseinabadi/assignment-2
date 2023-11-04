numbers = int(input("enter the number of fibbonacci: "))
num1, num2 =0,1
number_count = 0
if numbers <= 0:
   print("enter a positive number")

elif numbers == 1:
   print("fibonacci sequence",numbers)
   print(num2)
else:
   print("fibonacci sequence:")
   while number_count < numbers:
       print(num2)
       next_number = num1 + num2
       num1 = num2
       num2 = next_number
       number_count=number_count+1