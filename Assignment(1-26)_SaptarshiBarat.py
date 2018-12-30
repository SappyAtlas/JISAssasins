#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Question..1
class Count:
    def counting(self,num):
        x=num
        i=0
        e=0
        o=0
        z=1
        count=4
        while(count>0):
            z=x%10
            if z==0:
                i+=1
            elif z%2==0:
                e+=1
            elif z%2 !=0:
                o+=1
            x=x//10
            count-=1
        print("Zeroes={},Evens={}, Odds={}".format(i,e,o))
        
c=Count()
num=int(input("Enter a four digit number:"))
c.counting(num)


# In[2]:


##Question..2
num = []
n=int(input("How many numbers u want to enter"))
for i in range(1,n+1,1):
    x=int(input("Enter a number :"))
    num.append(x)
print("the number in the array are ",num) 
print("Max number in array is ",max(num))
print("Min number in arrat is ",min(num))
    


# In[3]:


##Question..4
num = int(input("How many figures:"))
storage = []
result = []
for i in range (1,num+1):
    a = int(input("Enter value" + str(i) + " : "))
    storage.append(a)
for m in range(len(storage)):
    b = min(storage)
    storage.remove(b)
    result.append(b)
j = ' '.join(str(i) for i in result)
print(j)


# In[4]:


##Question..6
names=[]
n=5
for x in range(1,n+1,1):
    names.append(input("Enter the names:"))
names.sort()
print("Names after sorting are",names)


# In[5]:


##Question..7
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)


# In[9]:


##Question..9
n = int(input("Enter a Number :"))

p = 0
f = 0
s = 0

l = n % 10

while n > 0:
    r = n % 10

    p= p * 10 + r

    n = int(n / 10)
    
f = p % 10

s = f + l

print("Sum of first and last digit is :", s)


# In[13]:


##Queston..8
x = int(input("Enter first number"))
y = int(input("Enter second number"))
def swap(w,v):
    return v,w
x,y=swap(x , y)
print(x)
print(y)


# In[12]:


##question..10
print("Enter 'x' for exit.")
string = input("Enter any string to remove all vowels from it: ")
if string == 'x':
    exit();
else:
    newstr = string;
    print("\nRemoving vowels from the given string...");
    vowels = ('a', 'e', 'i', 'o', 'u');
    for x in string.lower():
        if x in vowels:
            newstr = newstr.replace(x,"");
    print("New string after successfully removed all the vowels:");
    print(newstr);


# In[15]:


#Question..11
str = input("Enter the string")
char = input("Enter the character whose number of occurence is to be found in the string")
c = str.count(char)
print("Number of occurence of {} is {}".format(char ,c))


# In[16]:


#Question..12
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
print("\n")


# In[17]:


#Question..13
matrix1 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
matrix2 = [[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]]
rmatrix = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] + matrix2[i][j]
for r in rmatrix:
    print(r)


# In[6]:


#Question..14
from collections import Counter
z=[]
x=int(input("Enter the number of inputs u want to give"))
for y in range(x):
    a=int(input("Enter the number"))
    z.append(a)
Counter(z)


# In[ ]:


#Question..15
import math
x= int(input("Enter  X :"))
y= int(input("Enter Z :"))
z= int(input("Enter Y:"))
a= y + z
b = pow(x,a)
print("The result is",b)


# In[7]:


#Question..16
x= input("Enter the input :")
n= ord(x)
prev= n - 1
next= n + 1
a=chr(prev)
b=chr(next)
print(" ASCII value is : ",n)
print("The previous value is : ",a)
print("The next value is : ",b)


# In[8]:


#Question..17
x= input('enter the set of numbers :(enter space seperatedvalue):')
list1= x.split(" ")
res=[]
for i in list1:
    n = int(i)
    for j in range(2,int(n/2)):
        if(n%j == 0):
            break
    else:
        res.append(n)
print(res)


# In[10]:


#Question..23
X = input("Enter your string")
l=len(X)
print("The length is", l)
Y = "Saptarshi"
Z= X+Y
print("After concatenation", Z)
print(''.join(reversed(X)))
old="I like Python"
new=old.replace("like","love")
print(new)
if X == Y:
    print("Equal")
else:
    print("Not Equal")


# In[11]:


#Question..18
num=int(input("enter a number"))
num2=int(input("enter 2nd number"))
a=1
for num2 in range (1,num2+1):
    a=(a*num)
print(a)


# In[12]:


#Question..19
a=int(input("enter the first side of a triangle"))
b=int(input("enter the second side of the triangle"))
c=int(input("enter the third side of the triangle"))
if (a+b>c):
    print("triangle is valid")
elif (b+c>a):
    print("triangle is valid")
elif (c+a>b):
    print("triangle is valid")
else:
    print("triangle is not valid")
 


# In[13]:


#Question..20
msg="python is cooler java"
newmsg=msg.replace("a","@")
print(newmsg)


# In[14]:


#Question...24
num =int(input("enter a number"))
for i in range(1, 11):
   print(num,'x',i,'=',num*i)
 
    


# #Question..25
# num =int(input("enter a number"))
# for i in range(1, 11):
#    print(num,'x',i,'=',num*i)
#  

# In[ ]:


#Question...25
ch = input("Enter a character: ")
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
    print(ch, "is an Alphabet")
else:
    print(ch, "is a digit")


# In[1]:


#Question..26
bs = int(input("enter basic salary.\n"))
if bs >= 5000:
    hr = (15 / 100) * bs
    da = (150 / 100) * bs
else:
    hr = (10 / 100) * bs
    da = (110 / 100) * bs
g= bs + hr + da
print("basic salary", bs, "hra is", hr, "da is", da, "gross salary is", g)
  
 


# In[3]:


#Question..22
Books=[]
books1=[]
book=int(input("enter the no of books"))
for x in range(book):
    book_title=(input("enter the book title"))
    Books.append(book_title)
    author=input("enter the author of the book")
    Books.append(author)
    publisher=(input("enter the publisher"))
    Books.append(publisher)
    cost=int(input("enter the cost of the book"))
    Books.append(cost)
    accesion_no=int(input("enter the accession no to the book"))
    books1.append(accesion_no)
books1.sort()
print("The sorted books: {}".format(books1))
if cost>500:
    print("the books whose cost more than 500: BOOK TTITLE: {} BOOK AUTHOR:{} BOOK PUBLISHER:{} BOOK COST:{}".format(book_title,author,publisher,cost))
else:
    print("the books cost are less than 500:BOOK TTITLE: {} BOOK AUTHOR:{} BOOK PUBLISHER:{} BOOK COST:{}".format(book_title,author,publisher,cost))

print("BOOK TTITLE: {} BOOK AUTHOR:{} BOOK PUBLISHER:{} BOOK COST:{}".format(book_title,author,publisher,cost))


# In[1]:


#Question..5
class Customers:
    Bank=[]
    customers=int(input("enter no of customers(max 20) in the bank"))
    for x in range(customers):
        account_no=int(input("enter the a/c no. of the customer in the bank"))
        Bank.append(account_no)
        name=input("enter the name of the customer in the bank")
        Bank.append(name)
        balance=int(input("enter the balance of the customer"))
        Bank.append(balance)
        account=(input("enter the a/c running status"))
        Bank.append(account)
        def Account(self,balance):
            if balance<100:
                print("the account no : {} the name of customer: {} the balance of customer: {}".format(self.account_no,self.name,balance))
            else:
                print("the balance of customer is greater than 100")
C=Customers()
C.Account(balance=36)


# In[2]:


#Question..3
class Book:
    def id1(self):
        self.id_num=int(input("Please enter id\n"))
    def cost(self):
        self.book_cost=int(input("Please enter cost\n"))
    def author(self):        
        self.auth_name=input("Please enter author\n")
    def bookdb(self):
             print("BOOK ID: {} BOOK COST:{} BOOK AUTHOR:{} ".format(self.id_num,self.book_cost,self.auth_name))
b=Book()
b.id1()
b.cost()
b.author()
b.bookdb()


# In[ ]:


#Question..21
lists=[]
list1=[]
student=int(input("enter the no of students"))
for x in range(student):
    roll_no=int(input("enter the rollno"))
    lists.append(roll_no)
    stud_name=input("enter the name")
    lists.append(stud_name)
    marks1=int(input("enter the marks of the first subject"))
    list1.append(marks1)
    marks2=int(input("enter the marks of the 2nd subject"))
    list1.append(marks2)
    marks3=int(input("enter the marks of the 3rd subject"))
    list1.append(marks3)
    Total=0
    Average=0
    Total=marks1+marks2+marks3
    Average=Total/3
    print("the total marks of the student is ")
    print(Total)
    print("the average marks of the student")
    print(Average)
list1.sort(reverse=True)
print("the descending order of marks is :")
print(list1)
print("the names and roll no of students are:")
print(lists)


# In[ ]:




