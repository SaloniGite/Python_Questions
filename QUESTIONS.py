# Q1

# a= int(input("enter the no:"))
# print(a)

# Q2

# a="Name"
# b="is"
# c="james"
# print(a,b,c,sep="**")        #we use \ for the getting the ""

#Q3

# q = float(input("enter the float of two decimal :"))
# print(round(q,2))   #we use round for making float for 2 decimal place 

#Q4&Q5

# a = int(input("enter the no 1"))
# b = int(input("enter the no 2"))
# sum = a+b
# print("the sum of {} and {} is {}".format(a,b,sum) )
#  print(f"the sum of {a} and {b} is { sum }")

# Q6

# u = input("enter the username ")
# a = int(input( " enter the age "))
# print(f"Hello{u} , you are {a} years old ")

# Q7
# l = int(input("enter the length "))
# b =int(input("enter the breath"))
# area = l*b
# peimeter = 2*(l+b)
# print(f"the area is {area} and the perimeter is {peimeter}")

# m = int(input ("enter the maths marks :"))
# c = int(input ("enter the computer marks :"))
# e = int(input ("enter the english marks :"))
# TotalMarks = m +c+e
# per = round(((TotalMarks)/300)*100,2)

# print(f"the total marks are {TotalMarks} and percentage is { per}% ")

# Q9

# f= int(input( "enter the temp in farehnheit"))
# C=( (f-32)*5)/9
# print(round(C,3))

# Q10

# a= int(input("enter the amount"))
# t= int(input("enter the time"))
# r = int(input("enter the rate "))
# si = (a*t*r)/100
# print("the simaple intrest is " , si)

# Q11

# a= int(input("enter the no "))
# b= int(input("enter the no "))
# c= int(input("enter the no "))

# if(a==b):
#     print("a and b are equal")
# elif(b==c):
#     print("b and c are equal ")
# elif(a== b and b==c ):
#     print("all are equal")
# else:
#     print("none are equal")

# Q12
# a= int(input("enter the no "))
# b= int(input("enter the no "))
# if(a>b):
#     print("a is gratest ")
# elif(b> a):
#     print(" b is greatest ")
# else:
#     print("the are equal ")

# Q13 /14 
# u = input("enter the character m /f :")
# if(u=="m"):
#     print("the user is male ")
# elif(u=="f"):
#    print("the user is female ") 
# else:
#     print("invalid entry fill again ")

# # Q15
# a = int(input("enter the integer "))
# if(a%2 == 0):
#     print("its an even no")
# else:
#     print("its odd no ")

# Q16
# u = input("enter the name ")
# a = int(input("enter the age"))
# if(a<18):
#     print("not eligible")
#     print(f"you can vote in {18-a} yrs")
# else:
#     print("eligible")

# Q17

# p= int(input("enter the principal"))
# r= int(input("enter the rate"))
# n= int(input("enter the no"))
# t= int(input("enter the time"))
# ci = p*(1+(r/n))**n*t
# print("the compund intrest is " ,ci)

# Q19

# a=int(input("enter the no "))
# b=int(input("enter the no "))
# c=int(input("enter the no "))

# if(a>b and a>c):
#     print("a is greatest")
# elif(b>a and b>c):
#     print("b  is greatest")
# else:
#     print( " c is greatest")

#Q18

# a = int(input("enter the day no"))
# if(a == 1):
#     print("sunday")
# elif(a==2):
#     print("monday")
# elif(a==3):
#     print("Tuesday")
# elif(a==4):
#     print("wednessday")
# elif(a==5):
#     print("Thursday")
# elif(a==6):
#     print("Friday")
# elif(a==7):
#     print("saturday")
# else:
#     print("invalid no again try !!")

# Q 20
# a = int(input("enter the year "))
# if(a % 4==0 and a % 100 != 0):
#     print("leap year ")
# elif(a%100==0 and a%400==0):
#     print("leap yr")
# else:
#     print("not leap  yr")

# Q21
# m = int(input("enter the marks "))
# if(m>90 and m <=100):
#     print("AA")
# elif(m>80 and m <=90):
#     print("AB")
# elif(m>70 and m <= 80 ):
#     print("BB")
# elif(m>60 and m <=70):
#     print(  "BC")   
# elif(m>50 and m <=60):
#     print("CD")
# elif(m>40 and m <= 50) :
#     print("DD")
# elif(m>0 and m<+40):
#     print("F")
# else:
#     print("not valid marks")


# Q22

# a = input("enter the a letter ")
# if(a=="a" or a=="e" or a=="i" or a=="o" or a=="u"):
#     print("vowel")
# else:
#     print("consonant")

#Q23
 
# SWAPPING WITH THIRD VARIABLE
# a=19
# b=16
# c=b
# b=a
# a=c

# print(a)
# print(b)

# SWAPPING WITHOUT THIRD VARIABLE
# x= int(input("enter the no x "))
# y= int(input("enter the no y"))

# x=x+y
# y=x-y
# x=x-y
# print(x)
# print(y)

# Q24
# n = int(input("enter the no "))
# for i in range(0,n):
#     print("hello world")
#     print(i)
# i=0
# while(i<n):
#     print("hello world")
# #     i=i+1

# Q25
# n = int(input("enter the no "))
# for i in range(1,n):
#     print(i)

# i = 0
# while(i<= n):
#     print(i)
#     i = i+1

# # Q26 for reverse we use -1 
# n = int(input("enter the no "))
# for i in range(n,0,-1):
#     print(i)

# i = n
# while(i>0):
#     print(i)
#     i = i-1

# 27
# n = int(input("enter the no "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# i = 1
# while(i<= 10):
#     print(f"{n} * {i} = {n*i}")
#     i = i+1

# 28
# sum = 0
# n = int(input("enter the no "))
# for i in range(0,n+1):
#     sum = sum+i
# print(sum)

# Q29
# n = int(input("enter the no "))
# product = 1
# for i in range(1,n+1):
#     product = product*i
# print(product)

# Q30
# n = int(input("enter the no "))
# sum_even = 0
# sum_odd = 0
# for i in range(1,n):
#     if(i%2 == 0):
#         sum_even = sum_even +i
#     else:
#         sum_odd = sum_odd + i
# print("the sum of even is",sum_even)
# print("the sum of odd is ",sum_odd)

# Q31
# n = int(input("enter the no "))
# for i in range(1,n+1):
#     if(i%3 == 0 or i%5 == 0):
#         print(i)

# Q32
# n = int(input("enter the no "))
# for i in range(1,n):
#     if(n%i == 0):
#         print(i)

# Q33
# n = int(input("enter the no"))
# sum = 0 
# for i in range(1,n):
#     if(n%i == 0):
#         sum = sum +i
# print(sum)

# Q34
# n = int(input("enter the no "))
# sum = 0
# for i in range(1,n):
#     if(n%i == 0):
#         sum = sum + i
# if(sum == n):
#     print("the no is perfect no ")
# else:
#     print("no its not a perfect no ")

# Q35

# n = int(input("enter the no "))
# while(n>0):
#     num = n%10
#     print(num)
#     n = n//10

# if want in orignal pattern 
# n = int(input("enter the no :"))
# dig = []
# while(n>0):
#     num = n%10
#     dig.append(num)
#     n = n//10

# for i in reversed(dig):
#     print(i)
# print(dig)

# Q36
# n = int(input("enter the no "))
# sum = 0 
# while(n>0):
#     num = n%10
#     sum = sum +num 
#     n = n//10

# print(sum)

# Q37
# n = int(input("enter the no "))
# count = 0
# for i in range(1,n):
#     if(n%i == 0):
#         count += 1
# if(count == 2):
#     print("prime no ")
# else:
#     print("composite no ")

# Q38 

# n = int(input("enter the no "))
# num = 0 
# while(n>0):
#     num = num * 10 + n % 10
#     n = n//10
# print(num)

# Q39
# n = int(input("enter the no "))
# duplicate = n
# num = 0 

# while(n>0):
#     num = num * 10 + n % 10 
#     n = n // 10
# if(num == duplicate):
#     print("pallindromic no ")
# else:
#     print("not pallindromic no ")

# Q40 specail / armstrong no 
# n = int(input("enter the no "))
# copy = n
# num = 0
# while(n>0):
#     dig = n%10
#     num = num + dig**(len(str(copy)))
#     n = n//10
   
# if(num == copy ):
#     print("special no ")

# else:
#     print("no")

# Q41
# n = int(input("enter the no "))
# copy = n
# total = 0

# while(n > 0):   
#     num = n%10
#  we need to set fact in while loap value changes for each digit 
    # fact = 1                
#     for i in range(1,num+1):
#         fact = fact*i
#     total = total + fact
#     n = n//10
# if(copy == total):
#     print("strong no ")
# else:
#     print("not strong no ")

# Q42
# n = int(input("enter the no :"))
# copy = n 
# sum  = 0 
# while(n >0 ):
#     num = n%10
#     sum = sum + num 
#     n = n//10
# if(copy % sum == 0 ):
#     print("harshad no ")
# else:
#     print("not harshad no ")

# Q44
# a = "hello"
# b = "lilo"
# if(a>b):
#     print("a is greater")
# else:
#     print("b is greater")

# COMAPRISION DONE ON BASIS OF THE ALPHABET NO 

# Q45
# a = "hello ji "
# b = "bhago ji "
# print(a+b)

# Q46
# str = input("enter the string ")
# print(len(str))

# str = "saloni "
# count = 0
# for i in str:
#     count += 1
# print(count)

# Q47
# a = "Saloni"
# print(a.upper())
# print(a[1])

# Q48
# a = "hello ji chighkhor"
# copy = a
# print(copy)

# a = "hello ji chughalkhor "
# copy = " "
# for i in a:
#     copy += i 
   
# print(copy)

# Q49
# a= "LOAHDHAKDIMKNAJSH"
# print(a.lower())

# Q50
# a = input("enter the word1 to join ")
# b = input("enter the word2 to join")
# c = "".join([a,b])
# print(c)

# Q51
# a = input("enter the string")
# lower=""
# upper = ""
# for i in a:
#     if i.islower():
#         lower += i
#     else:
#         upper += i
# print(lower+upper)

# Q52
# str =  "P@#yn26at^&i5ve"
# num = 0
# alpha= 0
# sym = 0 
# for i in str :
#     if i.isnumeric():
#         num += 1 
#     elif i.isalpha():
#         alpha += 1
#     else:
#         sym += 1
# print("the  num is",num)
# print("the  alpha is",alpha)
# print("the symbol is ",sym)

# Q53
# a = input("enter the str")
# rev = ""
# copy = ""
# for i in a:
#     rev = i+rev
#     copy += i
# print("the reversed str is",rev)
# print("the lower case is ",a.lower())
# print("the upper case is ",a.upper())
# print("the lenght of strs is ",len(a))
# print("the copy of str is ",copy)

# Q55
# a = input("enter the str1")
# b = input("enter the str2")
# def check(x,y):
#     equal = True
#     if(len(a) != len(b)):
#         equal = False
#         print("it is not equal")
#     else:
#         for i in range(len(a)):
#             if(a[i]!= b[i]):
#                 equal = False
#                 print("it is not equal ")
#                 break
#     if equal:
#         print("equal")
# check(a,b)

# Q56
# str = input("enter the string")
# count = 0
# for i in str:
#     if(i=="a" or i == "e" or i == "i" or i =="o" or i == "u" ):
#         count += 1
# print(count)

# Q57
# a = input("enter the string ")
# rev = ""
# for i in a :
#     rev = i+rev
# print(rev)

# Q58
# a = input("enter the string ")
# real = ""
# rev = ""
# for i in a:
#     rev = i + rev 
#     real += i
# if(rev == real ):
#     print("pallindrome")
# else:
#     print("not pallindrome")
# print(a)

# Q59
# taking one input 
# x= input("enter the element ")
# l = []
# l = x.split() # it is used for splitting the string on the basis of space or commas in a list
# l.append(x)  # due to append it also takes the whole string 
# print(l)

# TAKING MULTIPLE INPUTS 
# n = int(input("enter the no of element to be inserted in list"))
# l = []
# for i in range(n):
#     elem = input("enter the element ")
#     l.append(elem)
# print(l)

# Q60
# n = int(input("enter the no of element to be inserted :"))
# l =[]
# for i in range(n):
#     elem = input("enter the elements")
#     l.append(elem)
# print(list(reversed(l)))

# Q61
# n = int(input("enter the no of element : "))
# l = [0,1]
# a = l[0]
# b = l[1]
# c = 0
# for i in range(n):
#     c = a+b
#     a = b
#     b = c
#     l.append(c)
# print(l)

# Q62
# l = [23 , -33 , 98 , -45 , 99]
# neg = []
# pos = []
# for i in l:
#     if(i >=0):
#         pos.append(i)
#     else:
#         neg.append(i)
# print("the neg no are ",neg)
# print("the positive no are ",pos)

# Q63
# n = input("enter the elements ").split()
# n.sort()
# print(n)
# print(list(reversed(n)))

# n = input("enter the data ").split() #split takes it as the string so compare alphabetically ex : 5 and 20 it will see 5 greater 
# n.sort(reverse=True)
# print(n)
 
# n = input("enter the data ")
# n = [int(i) for i in n]
# n.sort(reverse=True)          #for int only 
# print(n)

# Q64
# n = int(input("enter the elements in the list "))
# l = []
# sum = 0
# for i in range(n):
#     elem = int(input("enter the data :"))
#     l.append(elem)
# print(l)
# for i in l:
#     sum = sum + i
# print(sum)
# print("+".join(map(str,l)),f" = {sum}") #map means the function will done to each elment of the iterable which is  l 

# Q65 
# n = int(input("enter the no of element in elements:"))
# l = []
# sum = 0
# for i in range(n):
#     elem = int(input("enter the elem "))
#     l.append(elem)
# for i in l:
#     sum +=i
# print(f"mean = {sum /len(l)}")

# Q66