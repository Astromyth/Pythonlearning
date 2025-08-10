#task 1 : Check if number is odd or even

a= int(input('enter the no: '))


if  a % 2 == 0 :
    print (f"{a} is Even number.")
else:
    print (f"{a} is odd number.")

# task 2     sum of intergers from 1 to 50 using loop

sum=0
for i in range(1,51):
       sum+= i
print('The sum of no 1 to 50 is : ' , sum )