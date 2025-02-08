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

# Q40 Alternate
# n = int(input("Enter the number: "))
# sum = 0
# length = len(str(n))

# for i in str(n):
#     sum += int(i) ** length

# print(sum)

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
# c = "".join([a,b]) # used to join the two strings 
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
# for i in l:   #here iterating over the list so we are calling the list directly
#     sum += i
# print(f"mean = {sum /len(l)}")

# Q66
# n = int(input("enter the no :"))
# l = []
# Maxi = 0
# index = 0
# for i in range(n):
#     elem = int(input("enter the element "))
#     l.append(elem)
# for i in range(len(l)) : #here we are iterating over the indexes of the list and value by l[i]
#     if l[i]>Maxi:
#         Maxi = l[i]
#         index = i
# print(Maxi,index)

# Q67
# n = int(input("enter the no of elements to ne inserter "))
# l = []

# for i in range(n):
#     elem = int(input("enter the element"))
#     l.append(elem)
# smallest = l[0]
# index = 0
# for i in range(len(l)):
#     if smallest > l[i]:
#         smallest = l[i]
#         index = i
# print(f"the smallest is {smallest} at index {index}")

# Q68
# n = int(input("enter the no of element to be inserted :"))
# l = []
# index = 0 
# index2 = 0
# maxx = 0
# maxx2 = 0
# for i in range(n):
#     elem = int(input("enter the elements "))
#     l.append(elem)
# for i in range(len(l)):
#     if(l[i] > maxx):
#         maxx2 = maxx
#         maxx = l[i]
#         index2 = index
#         index = i 
#     elif(l[i] > maxx2 and l[i] < maxx ):
#         maxx2 = l[i]
#         index2 = i 
# print(f"the greatest is {maxx} and index is {index}")
# print(f"the second greatest is {maxx2} index at {index2}")
        
#Q69
# n = int(input("enter the elements to be inserted :"))
# l = []
# flag = True
# for i in range(n):
#     elem  = int(input("enter the element "))
#     l.append(elem)
# for i in range(len(l)-1):
#     if l[i] <= l[i+1]:
#         continue
#     else:
#         flag = False
#         print("not sorted ")
# if flag == True:
#     print("sorted ")

# LIST
# l = [23,45,67,98,12]
# l[2] = 48
# print(l)

# Q70
# n = int(input("enter the no of elements to be inputed : "))
# l = []
# for i in range(n):
#     elem = int(input("enter the element :"))
#     l.append(elem)
# reverse_l = list(reversed(l))  #used for revsring of the list 
# if(l == reverse_l):
#     print("It is a pallindrome ")
# else:
#     print("not a pallindrome")

# FUNCTION QUESTIONS
# Q1 Square a Number: Write a function that takes a number and returns its square.

# def square(a):
#     return(a*a)
# s = square(2)
# print(s)

# Q2 Convert Celsius to Fahrenheit: Write a function that converts a temperature from Celsius to Fahrenheit.
# def temp(C):
#     F = ((C*(9/5))+32)
#     print(F)
# temp(12)

# Q3 Write a function that takes a number and returns whether it's even or odd.
# def no(a):
#     if(a%2 == 0):
#         print("the no is even ")
#     else:
#         print("no is not even")
# no(6)

# def no(a):
    
#     if(a%2 == 0):
#         return True
#     else:
#         return False
# if no(4):
#     print("even")
# else:
#     print("odd")

# Q4 Write a function that takes two numbers and returns the absolute difference between them.
# def diff(a,b):
#     return a-b
# d = diff(10,34)
# print(d)

# Q5 Simple Greeting: Write a function that takes a name as input and returns a greeting message, like "Hello, [name]!".
# def greet():
#     print("Hello , Good morning everyone ")
# greet()

# Q6 String Length: Write a function that returns the length of a given string.
# def length(a):
#     return(len(a))
# l =  length("salomi hite")
# print(l)

# Q7  Write a function that takes a string and returns it in all uppercase letters.
# def UPPER(a):
#     return(a.upper())
# up = UPPER("itss meee hahaha")
# print(up)


# Q8  Write a function that counts how many times a specific character appears in a string.
# def chr(a):
#     str = input("enter the string ")
#     count = 0 
#     for i in str:
#         if(i == a):
#             count += 1 
#     return(count)
# c = chr("a")
# print(c)

# Q9 Write a function that takes a sentence and counts the number of words in it.
# def word_count(sentence):
#     words = sentence.split()
#     count = len(words)
#     return(count)
# c = word_count("Hey  its been a long time ")
# print(c)

# Q10   Write a function to check if a given string is a palindrome (reads the same backward as forward).
# def pallindrome_checker(n):
#     copy = n 
#     num = 0
#     while(n>0):
#         num = num*10 + n%10
#         n = n//10 
#     if(num == copy):
#         return True
#     else :
#         return False
# if pallindrome_checker(222):
#     print("its a pallindrome")
# else:
#     print("not a pallindrome")

# Q11  Sum of List: Write a function that takes a list of numbers and returns the sum of all elements.
# def sum_l(a):
#     l = []
#     total = 0
#     for i in range(a):
#        num = int( input("enter the elem "))
#        l.append(num)
#     for i in l :
#         total = total+i 
#     return(total)
# s = sum_l(8)
# print(s)

# Q12 write a function that takes a list of numbers and returns their average.
# def avg_l(n):
#     l = []
#     total = 0 
#     for i in range(n):
#         num = int(input("enter the element:"))
#         l.append(num)
#     for i in l :
#         total= total + i
   
#     avg = total/len(l)
#     return(avg)
# avg = avg_l(4)
# print(avg)

# Q13 Write a function that takes a list of numbers and returns the smallest and largest numbers.
# def cal(n):
#     l = []

   
#     for i in range(n):
#         num = int(input("enter the element : "))
#         l.append(num)
#     maxx = l[0]
#     minn = l[0]
#     for i in range(len(l )):
#         if(maxx<l[i]):
#             maxx = l[i]
#         if(minn>l[i]):
#             minn = l[i]
#     return(maxx,minn)
# comp = cal(6)
# maxx , minn = comp 
# print(comp)
# print(f"the max is {maxx} and min is {minn}")

# Q14  Remove Duplicates: Write a function that takes a list and returns a new list with duplicates removed.
# def remove_duplicates(old_list):
#     new_list= []
#     for items in old_list:
#         if items not in new_list:
#             new_list.append(items)
#     return(new_list)
# list = [3,3,5 ,6 , 78, 4 ,3 ,5 ]
# mylist = remove_duplicates(list)
# print(mylist)

# Q15 Write a function that takes a list and returns it in reverse order.
# def rev(my_list):
#     return(list(reversed(my_list)))
# c_list = [2,3,4,5,6,7,8]
# s = rev(c_list)
# print(s)

# TUPLE (immutable can't be changed and when slicing done a new tuple is returned )
# a = ( 1, "saloni", 45 , True)
# print(type(a)) 

# b = (1)
# print(type(b))  #return int as type as compiler gets confused so we need to add a comma in it 

# ex:
# c = (3,)
# print(type(c))  # now it return the type as tuple

# a[2] = "meee"
# print(a)   # cant change 

# print(a[-1]) # len(a)-(1) = 4-1 = 3 which is True 

# print(a[1:3]) slicing is done same as list 

# TUPLE CAN BE CHANGED BUT NOT DIRECTLY WE NEED TO CONVERT THE TUPPLE INTO LIST THEN CONVERT LIST INTO TUPLE 
# T = (2 , 3 , 4 , 5 , 6, 7)
# Temp_list = list(T)
# Temp_list.append("saloni")
# Temp_list.pop(2)
# Temp_list[5] = "memememem"
# T = tuple(Temp_list)
# print(T)

# CONCATENATION CAN BE PERFORMED 
# T = ( 1 , 2, 3, 4,5, 6, 7,8)
# M = ("slaoni" , "hahah", "meee")
# new_tuple = T + M 
# print(new_tuple)

# COUNT
# no = (1,2,3,4,5,6,42,31,3,1,23,3)
# count_no = no.count(3)
# print(count_no)


# color = ("blue" , "green" , "yellow" , "blue")
# item_count = tuple.count("blue")
# print("item_count")  #count is not for str only for int 

# INDEX (gives the index of the first occurence tuple_name.index(element,start,end))
# print(no.index(31))
# print(no.index(3 , 7 , 11))

# LENGTH
# print(len(no))

# FABONACCI SERIES WITH RECURSIVE FUNCTION 
# def fibonacci(n):
#     if n <= 1:
#         return n  # Base case: return n if it's 0 or 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# # Driver code to display the series
# terms = int(input("Enter the number of terms: "))
# if terms <= 0:
#     print("Please enter a positive integer.")
# else:
#     print("Fibonacci Series:")
#     for i in range(terms):
#         print(fibonacci(i), end=" ")

# # FABONACCI SERIES WITH FUNC

# def FAB(n):
#     if n <= 0:
#         print("Provide a positive number.")
#     elif n == 1:
#         print("Fibonacci Series: 0")
#     elif n == 2:
#         print("Fibonacci Series: 0 1")
#     else:
#         a, b = 0, 1
#         print("Fibonacci Series:", end=" ")
#         print(a, b, end=" ")
#         for i in range(2, n):
#             c = a + b
#             print(c, end=" ")
#             a, b = b, c
#     return

# # Driver code
# terms = int(input("Enter the number of terms: "))
# FAB(terms)

# RECURSION
# Q1:Write a recursive function to reverse a string.
# def rev_str(s):
#     if len(s)==0:
#         return s
#     else:
#         return s[-1]+ rev_str(s[:-1])

# str = input("enter the string :")
# print(rev_str(str))

# Q2: Write a recursive function to find the sum of all elements in a list.
# def count_l(l):
#     if len(l) == 0:
#         return 0 
#     else:
#         return l[0] + count_l(l[1:])
# list_n = [23 ,45,56,67,68,98,99]
# print(count_l(list_n))

# Q3: Count Vowels in a String
# def count_vowel(str):
#     if len(str) == 0:
#         return 0
#     else:
#         return(1 if str[0].lower() in 'aeiou' else 0) + count_vowel(str[1:])
# print(count_vowel("dalojhaiofa"))

# Q4: Write a recursive function to find the smallest element in a tuple.
# def sm_elem(t):
#     if len(t) == 1:
#         return t[0]
#     else:
#         return min(t[0] , sm_elem(t[1:]))
# tm = (1,2,3,2,1)
# print(sm_elem(tm))

#Q5: Write a recursive function to check if a string is a palindrome.
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     return s[0] == s[-1] and is_palindrome(s[1:-1])



# 71) List left Rotation by 1

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# n = 1

# for i in range(n):
#     temp = l[0]
    
#     for j in range(len(l)-1):
#         l[j] = l[j+1]

#     l[len(l)-1] = temp

# print(l)

# 72) List right Rotation by 1

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# n = 1

# for i in range(n):
#     temp = l[len(l)-1]

#     for j in range(len(l)-1,-1,-1):
#         l[j] = l[j-1]
    
#     l[0] = temp

# print(l)

# 73) List left rotation by K elements

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# x = int(input("Enter the number of elements to rotate the list : "))

# for i in range(x):
#     flag = l[0]

#     for s in range(len(l)-1):
#         l[s] = l[s+1]

#     l[len(l)-1] = flag

# print(l)


# 74) List right rotation by K elements

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# x = int(input("Enter a number to rotate the list : "))

# for i in range(x):
#     flag = l[len(l)-1]

#     for s in range(len(l)-1,-1,-1):
#         l[s] = l[s-1]

#     l[0] = flag

# print(l)

# 75) List Reverse Using Extra space
# using extra space means that we can use another list that is empty as we have done previously

# l = [1,2,3,4,5,6,7]
# l2 = []

# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])

# print(l2)


# 76) List Reverse Without Using Extra space
# without using extra space means we can't store data in another list or empty variable

# l = [1,2,3,4,5,6,7,8,9,10]

# i = 0
# end = len(l)-1

# for i in range(len(l)//2):
#     l[i],l[len(l)-i-1] = l[len(l)-i-1],l[i]

#     i+= 1
#     end -= 1

# print(l)

#----------------------------------->>>> using while loop <<<<---------------------------------------------

# l = [1,2,3,4,5,6,7,8,9,10]

# i = 0
# s = len(l)-1

# while i < s:
#     l[i],l[len(l)-i-1] = l[len(l)-i-1],l[i]

#     i += 1
#     s -= 1

# print(l)

# 77) Linear Search an List - If element found print the index else -1

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61]

# x = int(input("Enter the element of the list u want to find : "))
# flag = False

# for i in range(len(l)):
#     if l[i] == x:
#         flag = True
#         break

#     else:
#         flag = False

# if flag == True:
#     print(f"The element {x} was found at index : {i}")

# else:
#     print(-1)

# 78) Binary Search. If element found print the index else -1

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61]

# x = int(input("Enter the element to find : "))
# i = 0
# s = len(l)-1
# flag = False

# while i < s:  # using 2 - pointer technique
#     if l[i] == x or l[s] == x:
#         flag = True
#         break

#     else:         # this is a two pointer method so can be applied when the list is not sorted and is not pure binary search
#         flag = False

#     i += 1
#     s -= 1

# if flag:
#     print(f"The element {x} was found at index : {i}")
# else:
#     print(-1)

# 79) Move all the negative elements on left side and positive elements on right side with extra space in O(n).

# l = [43, -12,-76, 32, -90, 54,-23, 67, 89, -14, 31, -78, 45,- 9, 61]
# l2 = []
# l3 = []

# for i in range(len(l)):
#     if l[i] < 0:
#         l2.append(l[i])

#     else:
#         l3.append(l[i])

# print(l2+l3)


# 80) Move all the negative elements on left side and positive elements on right side without extra space in O(n).

# l = [43, -12,-76, 32, -90, 54,-23, 67, 89, -14, 31, -78, 45,- 9, 61]

# i = 0
# s = len(l)-1

# while i <= s:
        
#     if l[i] < 0:
#         i += 1

#     elif l[s] >= 0:
#         s -= 1

#     else:
#         l[i],l[s] = l[s],l[i]
#         i += 1
#         s -= 1 

# print(l)


# 81) Bubble Sort.

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61]

# for i in range(len(l)):
#     for s in range(len(l)-1):
#         if l[s] > l[s+1]:
#             l[s],l[s+1] = l[s+1],l[s]

# print(l)

# 82) Median of List elements

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61,33]
# l.sort()
# n = len(l)

# if len(l) % 2 != 0:
#     median = (n-1)//2
#     mid = l[median]
    
# else:
#     median = n//2
#     median2 = median - 1
#     mid = (l[median] + l[median2])/2

# print("The median of the given list is",mid)

# 83) Strong number using methods

# x = int(input("Enter a number to check if its a strong number or not : "))
# copy = x
# sum = 0

# def factorial(a):
#     fact = 1
#     for i in range(1,a+1):
#             fact *= i
#     return fact

# while x > 0:
#       z = x % 10
#       sum += factorial(z)
#       x //= 10

# if sum == copy:
#       print("Yess It's a strong number......")

# else:
#       print("No.... It's not a strong number !!!!")

# 84) Number of even and odd elements in an List

# l = [43, 12, 76, 32, 90, 54, 23, 67, 89, 14, 31, 78, 45, 9, 61,33]

# count = 0
# count2 = 0

# for i in l:
#     if i % 2 == 0:
#         count += 1
#     else:
#         count2 += 1
    
# print(f"The number of ev

# for i in dict:
#     sum += dict[i]

# print("The sum of all the values in the dictionaty is",sum)

# 89) Convert a list to dictionary 


# 90) count the frequency of each elements

# dict = {'apple': 2, 'banana': 3, 'orange': 2, 'grape': 1, 'kiwi': 3}
# dict2 = {}

# for i in dict.values():             # .values() is used to get the values of the key
#     if i in dict2:
#         dict2[i] += 1 
    
#     else:
#         dict2[i] = 1

# print(dict2)



# 91) Write a Python program to combine two dictionary by adding values for common keys.

# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 5, 'c': 15, 'd': 25}

# dict3 = {}

# dict3 = dict1.copy()

# for i,s in dict2.items():
#     if i in dict3:
#         dict3[i] += s

#     else:
#         dict3[i] = s

# print(dict3)



# 92) replace the maximum appearing number in a list with 0

# dict = {'a': 5, 'b': 8, 'c': 5, 'd': 3, 'e': 8, 'f': 3, 'g': 5}
# dict2 = {}

# for i in dict.values():
#     if i in dict2:
#         dict2[i] += 1

#     else:
#         dict2[i] = 1

# max_appearing_value = max(dict2, key = dict2.get) # this line gives the maximum occuring key .get() is used to get value of the key

# for i,s in dict.items():
#     if dict[i] == max_appearing_value:
#         dict[i] = 0

# print(dict)


# 93) Right Triangle - Star

#       	*
#       	* *
# 	        * * *
#       	* * * *
#       	* * * * *

# x = int(input("Enter the number of rows in the pattern : "))

# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print("*",end="")
    
#     print(" ")


# 94) Right Triangle - Number

#    	1                            #   1
# 	    1 2                          #   22
# 	    1 2 3                OR      #   333
#   	1 2 3 4                      #   4444          
#   	1 2 3 4 5                    #   55555

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(1,x+1):
#     for j in range(1,i+1):          # 2nd loop me j lene pe 1st wala pattern aata h and i lene pe 2nd wala
#         print(j,end='')
    
#     print("")

# #------------------------------------------>>>>>  OR  <<<<<--------------------------------------------------
    
# x = int(input("Enter the number of rows t0 print the pattern : "))

# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(i,end="")

#     print("")

# 95) Right Triangle - Alphabet

#        	A                               # A
# 	        A B                             # BB
# 	        A B C            OR             # CCC
# 	        A B C D                         # DDDD
# 	        A B C D E                       # EEEEE

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(65,x+65):         # use ascii values for the alphabets and then convert them into the char form
#     for j in range(65,i+1):      # ascii values of A is 65
#         print(chr(j),end="")        
    
#     print("")

# # ================================>>>>> OR <<<<<==========================================

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(65,x+65):
#     for j in range(65,i+1):
#         print(chr(i),end="")

#     print("")

# 96) Inverted Right Triangle

#    	* * * * *
#   	* * * *
#   	* * *
#   	* *
# 	    *

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x-1,-1,-1):
#     for j in range(i,-1,-1):
#         print("*",end="")
#     print("")


# 97) Mirrored Right Triangle

# 	            *
# 	          * *
# 	        * * *
# 	      * * * *
#   	* * * * *

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x):

#     for j in range(x-i-1):
#         print(" ",end="")

#     for j in range(i+1):
#         print("*",end="")

#     print()

# =================================>>>>> using single for loop <<<<<=============================================

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x):
#     print(" "*(x-i-1) + "*"*(i+1))  # this is string multiplication method


# 98) Mirrored Inverted Right Triangle

#      	* * * * *
#   	  * * * *
# 	        * * *
# 	          * *
# 	            *

# x = int(input("Enter the number of rows to print the pattern : "))

# for i in range(x+1):
#     print(" "*(i+1) + "*"*(x-i))

# ------------------------------------------------>>>> OR <<<<----------------------------------------------------

# x = int(input("Enter the number of rows to print the pattern : "))
# k = 0
# z = x

# for i in range(1,x+1):
        
#     print(" "*k,"*"*z,end="")
#     k += 1
#     z -= 1 
#     print()
