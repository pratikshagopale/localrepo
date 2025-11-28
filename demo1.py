# swaping no

'''num1= input("enter the num1")
num2= input("Enter num2")

print("The num one is",num1)
print("The num two is",num2)

num1, num2= num2, num1

print(num1)
print(num2)'''

# no is prime or not
# condition is number is divided by 1 or itself

'''num= int(input("enter number"))
count=0   # how many counts

if num>1:
    for i in range(1,num+1):
        if (num%i) == 0:
            count=count+1
    if count ==2:
        print("num is prime")
    else:
        print("num is not prime")'''


#fatorial
# fact =1
# num= 10
#
# if num<0:
#     print("negative no is does not exist")
#
# elif num==0:
#     print("the factorial of zero is  1")
#
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#     print("factorial of",num,"is",fact)

#approch 2 using recursive function
# def facto(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*facto(n-1)
# num=10
# print("frctorial of",num,"is",facto(num))

#or in sigal statment
# def fact(n):
#     return 1 if(n==1 or n==0) else n* fact(n-1)
# num=10
# print("frctorial of",num,"is",fact(num))

#fibinocy series

n1=0
n2=1
print(n1)
print(n2)
for i in range(2,10):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
    #0 1   1 2 3 5 8
       #n1 n2












