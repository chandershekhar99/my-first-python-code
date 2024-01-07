#!/usr/bin/env python
# coding: utf-8

# # STRING
String is a sequence of charecter .string can be created by emclosing characters inside quote or double qoutes

# In[2]:


a="welcome to my world"
t=len(a)
print(a)
for n in range(t):
    print(a[n])


# In[4]:


a="welcome to my world"
for n in a:
    print(n)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # data type

# In[25]:


a=24
print(type(a))
'''flaot'''
b=23.43
print(type(b))
'''str'''
c='shekhar' 
print(type(c))
'''boolen'''
d=4
e=5
c=d>e
print(c)
type(c)


# In[ ]:





# INTEGER= it is any number.po
# sitive or negstive number without decimal of unlimited length
# 

# In[14]:


a=23
print(type(a))


# string method

# In[4]:


a="hello world i am chandrashekhar"
print(a)


# In[5]:


a.upper()


# In[6]:


a.lower()


# In[8]:


len(a)


# In[12]:


a. islower()


# In[13]:


a.isupper()


# In[14]:


a.capitalize()


# In[15]:


a.replace("h","kh")


# In[16]:


a.title()


# In[17]:


a.count("a")


# In[18]:


a[2:22]


# In[19]:


a[-1::-1]


# It is represent one of tow value true or fales

# In[1]:


a="shekhar"
print(a)


# In[2]:


a="True"
print(type(a))


# In[3]:


a=23
print(a)


# In[4]:


a="False"
print(type(a))


# In[1]:


a="shekhar"
print(type(a))


# In[2]:


a=input("Enter your age")
new_age=int(a)+3
print(new_age)


# In[3]:


age=23
if age>18:
    print("you can't vote")
else:
    print()


# In[4]:


a=int(input("enter the first num"))
b=int(input("enter the second num"))
c=a+b
print(c)


# In[ ]:





# In[ ]:





# In[ ]:





# # OPERATORS IN PYTHON
OPERATOR= oprater are special type  symbol in python that carryout arithmetic or logical computation.the value that are opretor on is called the oprend.  ARITHMETIC OPERATION=
# In[3]:


a=34
b=43
c=a+b
print(c)


# In[4]:


a=int(input("enter the number = "))
b=int(input("enter the number = "))
c=a+b
print(c)


# In[8]:


a=34,24,67,87
b=23,56,43,45
c=a+b
print(type(c))


# In[6]:


a=34
b=25
c=a-b
print(c)


# In[9]:


a=int(input("enter the number = "))
b=int(input("enter the number = "))
c=a-b
print(c)


# In[10]:


a=45
b=7
c=a*b
print(c)


# In[11]:


a=5556
b=2
c=a//b
print(c)


# In[12]:


a=3452
b=3
c=a/b
print(c)


# In[13]:


a=3452
b=3
c=a/b
print(c)


# In[2]:


import this


# Declearation of variable

# In[11]:


s=input()


# In[12]:


s


# In[14]:


s=input("what is  your name? ")


# In[15]:


print(s)


# In[7]:


name=input("what is your name?")
print("hello",name)
age=input("how old are you?")
print("your age",age,"years old")


# In[15]:


a="Guloo"
a.lower()
'''upper'''
b="guloo"
b.upper()


# In[16]:


b="guloo"
b.upper()


# math function

# In[19]:


abs(-23)


#  

# In[22]:


pow(4,3)


# In[23]:


l=round(4353.5343)
round(l,3)


# solve

# step1
input a value from the user and keep it in variable a.
input an other value from the user and keep it in varible b.
print the product of tow value(a*b).

# # conditional statement

# boolean expre.

# In[27]:


a=34
b=34
if a==b:
    print("a is equal b")


# In[28]:


a=23
b=12
if a>b:
    print("a is geater than b")


# In[3]:


age= 23
if age>19:
    print("you can vote ")


# In[4]:


age=32
if age<19:
    print("you can vote")
else:
    print("you can't vote")


# In[5]:


age=22
if age>18:
    print("vote krne chalo bhai")
elif age==22:
    print("first time voter")
else:
    print("sorry ap vote nhi kr skte")

Wap to find the odd & even value.
Wap to find a individual is child or adult.
Wap to find if its rainy outside or not.
write a condition is if tempreture is 45 degree
than it is raining 
# In[11]:


a=67
if a%2==0:
    print("even")
else:
    print("odd")


# In[14]:


a=18
if a%3==0:
    print("even")
else:
    print("odd")


# In[16]:


a=int(input("enter you age"))
if a>18:
    print("you are adulte")
else:
    print("your not adult")


# In[17]:


temp=int(input("enter a value"))
if temp==35:
    print("it is rainyday")
else:
    print("not  rainyday")


# In[19]:


day=input("enter day name =")
if day=="sunday":
    print("today is holiday")
else:
    print("boring day")


# In[21]:


marks=int(input("entar a number= "))
if marks>80:
    print("high marks")
elif marks>80 and marks<92:
    print("good marks")
elif marks>75 and marks<80:
    print("avarage marks")
elif marks>55 and marks<75:
    print("pass")
else:
    print("fail")


# In[23]:


marks=int(input("entar a number= "))
if marks>80:
    print("high marks")
elif marks>80 and marks<92:
    print("good marks")
elif marks>75 and marks<80:
    print("avarage marks")
elif marks>55 and marks<75:
    print("pass")
else:
    print("fail")


# In[24]:


marks=int(input("entar a number= "))
if marks>80:
    print("high marks")
elif marks>80 and marks<92:
    print("good marks")
elif marks>75 and marks<80:
    print("avarage marks")
elif marks>55 and marks<75:
    print("pass")
else:
    print("fail")


# In[15]:


exp=int(input("enter a exp= "))
sal=int(input("enter a sal= "))
if exp==8:
    bonus=sal*6%100  
    totalsalary=sal+bonus
    print("bonus amount=",bonus)
else:
    print("no more bonus")


# In[1]:


hl_class=int(input("enter class h= "))
at_class=int(input("enter class a= "))
per_attend_class=(at_class/hl_class)*100
print(per_attend_class)
if per_attend_class>75:
    print("allow")
else:
    print("dont allow")


# In[ ]:


num=int(input("enter the number?"))
if num%2==0:
    print("number is even..?")
else:
    print("number is odd..?")


# In[ ]:


age=int(input("enter the age="))
if age>=20:
    print("you are eligible to vote!!")
else:
    peint("Sorry! you have to wait")


# In[ ]:


a=21
b=67
c=43
if a<b and a>c:
    print("A")
if b>a and a>c:
    print("B")
if c>a and c>b:
    print("C")


# In[ ]:


num=int(input("enter the number"))
if num%2==0:
    print("number is even")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # looping
loop eapeat any opration again and again
it is tow type=for loop and while loop.
Wap to print number from 1 to 10.
Wap to print number from 2 to 9.
Wap to print number from 1 to 50.
try to print number in alternative way.
# In[3]:


for i in range (1,10):
    print(i)


# In[5]:


for i in range(2,9):
    print(i)


# In[6]:


for i in range(1,51,2):
    print(i)

Wap to print -1 to 10.
Wap to print even number from 1 to 50.
Wap to print  odd number from 20 to 80.
# In[1]:


for i in range(-10,-1):
    print(i)


# In[2]:


for i in range(1,51):
    print(i)


# In[3]:


for i in range(1,51):
    if i%2==0:
        print(i)


# In[1]:


count=0
for i in range(20,80):
    if i%2==0:
        print(i)
        count=count+1
        print("count--->", count)


# In[1]:


x='shekhar'
for i in range x:
    print(i)
    y=i=y
    


# write a program to find the add and even number

# In[2]:


a=int(input("enter the no ="))
b=int(input("enter the no =")) 
c=int(input("enter the no ="))
avg=(a+b+c)/8
print(avg)


# In[4]:


age=21
if age>21:
    print("you can vote ")
elif age==21:
    print("first time vote")
else:
    print("no vote")


# In[6]:


age=21
if age>21:
    print("you can vote ")
elif age!=21:
    print("first time vote")
else:
    print("no vote")


# write a program to find the odd and even number.

# In[16]:


a=67
if a%2==0:
    print("even number")
else:
    print(" odd number")


# In[17]:


a=67
if a%21!=0:
    print("even number")
else:
    print(" odd number")


# write a program to find a individule value is child are adult

# In[4]:


a=int(input("enter the no ="))
if a>18:
        print("adult")
else:
        print(" not adult")


# In[5]:


a=int(input("enter the no= "))
b=int(input("enter the no= "))
c=int(input("enter the no= "))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("invailed")


# In[6]:




a=int(input("enter the no= "))
b=int(input("enter the no= "))
c=int(input("enter the no= "))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("invailed")


# loop = reapet any program again and again and give a boolen value true ao false
write a program to print a number from 2 to 9 with the help of for loop.
# In[7]:


for i in range(1,10):
    print(i)


# In[8]:


for i in range(1,51,2):
    print(i)

write a program to print (1to10) with the help of while loop.
# In[14]:


x=10
while x<12:
    print(x)
    x=x+1


# In[15]:


x=50
while x<70:
    print(x)
    x=x+1

write a program print even number 1 to 50
# In[17]:


count= 0
for  i in range (1,50):
    print(i)
    count=count+1
    print("count----->",count)

write a program to print a reserve or not.
# In[21]:


a='shekhar'
b=''
for i in a:
    print("a")
    b=i=b
    print("b")
if a!=b:
    print("reseversed")
else:
    print("not reserversed")

Data collection it is 4 type=list , tuple, dict,set.
# # list

# In[24]:


a=[43,34,65,78]
print(a)
type(a)


# In[25]:


a=[43,34,65,78]
b=0
for i in a:
    b=i+b
    print(b)

list method=append, index,pop,remove,short,reverse.    
# # append

# In[8]:


x=[34,54,64,23]
x.append("shekhar")


# In[9]:


a=[(56,43,78,69)]
y=lambda a:a
a.append(5)
a


# In[ ]:




