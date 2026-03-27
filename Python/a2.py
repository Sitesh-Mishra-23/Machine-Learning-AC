#1
# salary = int(input("Enter Your Salary : "))
# if(salary<30000):
#     print(f"tax rate is 5 % and your salary after deduction is  {salary-((5*salary)/100)}")
# elif(salary>30000 and salary<70000):
#     print(f"tax rate is 15 % and your salary after deduction is  {salary-((15*salary)/100)}")
# else:
#     print(f"tax rate is 25 % and your salary after deduction is  {salary-((25*salary)/100)}")

#2
# def even_print(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i," ")

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# even_print(a,b)

#3
# def digit_print(num):
#     while(num>0):
#         digit = num%10
#         print(digit)
#         num=num//10

# num=int(input("Enter number:"))
# digit_print(num)

#4
# def digit_count(num):
#     count=0
#     while(num>0):
#         digit = num%10
#         count+=1
#         num=num//10
#     print("Digit count is:",count)

# num=int(input("Enter number:"))
# digit_count(num)

# 5
# def sum_count(num):
#     sum=0
#     while(num>0):
#         digit = num%10
#         sum+=digit
#         num=num//10
#     print("Sum of each digit in numberis:",sum)

# num=int(input("Enter number:"))
# sum_count(num)

# 6
# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print(i)

# 7
# while True:
#     choice=input("Do you want to quit ? enter quit")
#     if(choice=="quit"):
#         break
#     else:
#         num=int(input("Enter number:"))
#         if num > 0:
#             print("Positive")
#         else:
#             print("Negative")

#8
# def calculator(a,b,op):
#     if(op=="+"):
#         print(a+b)
#     elif(op=="*"):
#         print(a*b)
#     elif(op=="/"):
#         print(a/b)
#     else:
#         print(a-b)

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# op=input("Enter operation:")
# calculator(a,b,op)
    
#9
# def is_prime(num):
#     prime = True
#     for i in range(2,num):
#         if(num%i==0):
#             prime=False
#         else:
#             continue
#     return prime
        
# num=int(input("enter number:"))
# if(is_prime(num)):
#     print("Number is prime")
# else:
#     print("number is not prime")

#10
# while True:
#     num=69
#     guess=int(input("Enter your guess number:"))
#     if(num==guess):
#         print("Correct")
#         break
#     elif(num<guess):
#         print("lower")
#     else:
#         print("higher")