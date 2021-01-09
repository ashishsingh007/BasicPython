#!/usr/bin/env python
# coding: utf-8
*******Never Ever Gip Up Man*******
# In[2]:


print(dir(str))


# In[3]:


print(help(str))


# In[14]:


tempStr = str('Ashish')


# In[17]:


tempStr.__add__(' Singh')


# In[18]:


tempStr.__len__()


# In[22]:


tempStr.__contains__('Ashish')


# In[34]:


#str.capitalize()    
#Return a copy of the string with its first character capitalized and the rest lowercased.
tmpStr ='Atul singh'
tmpStr.capitalize()


# In[44]:


#str.casefold()
#Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
tmpStr ='ss'
tmpStr.__eq__('ss')


# In[56]:


#str.center(width[, fillchar])
#Return centered in a string of length width. Padding is done using the specified 
#fillchar (default is an ASCII space). The original string is returned 
#if width is less than or equal to len(s).
tmpStr ='4005'
tmpStr.center(10,'0')


# In[67]:


#str.count(sub[, start[, end]])
#Return the number of non-overlapping occurrences of substring sub in the range 
#[start, end]. Optional arguments start and end are interpreted as in slice notation.
tmpStr='ashish singh, How are you'
tmpStr.count('a',6,19)
#tmpStr[18]


# In[76]:


#str.endswith(suffix[, start[, end]])
#Return True if the string ends with the specified suffix, 
#otherwise return False. suffix can also be a tuple of suffixes to look for. 
#With optional start, test beginning at that position. With optional end, stop comparing 
#at that position.
tmpStr='ashish singh, How are you1,aa'
tmpStr.endswith(('a','u'),-3,)


# In[80]:


#str.find(sub[, start[, end]])
#Return the lowest index in the string where substring sub is found within the 
#slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. 
#Return -1 if sub is not found.
tmpStr='ashish singh, How are you1,aa'
tmpStr.find('w',17)


# In[81]:


print('{}, {}. How are you'.format('Hello','Ashish'))


# In[97]:


a='Hello'
b='Ashish'
print(f"{'Hello'.lower()}, {b}. How are you")


# In[92]:


name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
           f"Hi {name}. "
           f"You are a {profession.capitalize()}. "
           f"You were in {affiliation.casefold()}."
)
message.lower()


# In[112]:


#str.index(sub[, start[, end]])¶
#Like find(), but raise ValueError when the substring is not found.
tmpStr='ashish'
#tmpStr.index('w',16)


# In[117]:


tmpStr='ashish12'
tmpStr.isalnum()


# In[120]:


tmpStr='ashish'
tmpStr.isalpha()


# In[132]:


tmpStr='5/2'
tmpStr.isdecimal()
#tmpStr.isdigit()
#tmpStr.isnumeric()


# In[169]:


lst =['Ashish','atul','1000','Alka12','100',200.0]


# In[172]:


strcount,nbrcount,fltcount,dgtcount=0,0,0,0
for x in lst:
    if isinstance(x,int):
        nbrcount+=1
    elif isinstance(x,float):
        fltcount+=1
    elif x.isdigit():
        dgtcount+=1
    else:
        strcount+=1
    
print(f"String count is {strcount}. \n" 
      f"Number,float count is {nbrcount,fltcount}. \n"
      f"Digit count is {dgtcount}.")


# In[182]:


#str.join(iterable)
#Return a string which is the concatenation of the strings in iterable. 
#A TypeError will be raised if there are any non-string values in iterable,
#including bytes objects. The separator between elements is the string providing this method.
tpl=('200','ashish','Temp_001',100.0,200)
temp=''
temp.join(str(tpl))


# In[188]:


tmpStr='40045'
x=tmpStr.rjust(10,'0')


# In[190]:


x.split(',')


# In[ ]:


##There are many more methods available but will explore them later


# In[200]:


#Exercise Question 1: Given a string of odd length greater 7, 
#return a string made of the middle three chars of a given String
#Case 1 - str1 = "JhonDipPeta"
str1 = "JaSonAy"
def functionTogetMiddleValue(argStr : str):
    middlevalue= int(len(str(argStr))/2)
    print('Original String passed by usre is : '+ argStr)
    print(argStr[middlevalue-1:middlevalue+2])

functionTogetMiddleValue(str1)


# In[207]:


#Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
s1 = "Ault"
s2 = "Kelly"
def appenMiddle(str1,str2):
    middleValueCnt=int(len(str1)/2)
    print(f"First string {str1} and Second string {str2} passed in function.")
    outPutStr=str1[:middleValueCnt]+str2+str1[2:]
    print(f"New string is {outPutStr}")

appenMiddle(s1,s2)


# In[214]:


#Given 2 strings, s1, and s2 return a new string made of the first, 
#middle and last char each input string
s1 = "America"
s2 = "Japan"
ex="AJrpan"
def newString(str1,str2):
    Cnt1=int(len(str1)/2)
    Cnt2=int(len(str2)/2)
    print(f"First string {str1} and Second string {str2} passed in function.")
    outPutStr=str1[0]+str2[0]+str1[Cnt1]+str2[Cnt2]+str1[-1]+str2[-1]
    print(f"New string is {outPutStr}")

newString(s1,s2)


# In[217]:


# Arrange string characters such that lowercase letters should come first
str1  = 'PyNaTive'
exptd = 'yaivePNT'
lstr=''
ustr=''
for x in str1:
    if x.islower():
        lstr+=x
    else:
        ustr+=x
print(lstr+ustr)


# In[239]:


#Count all lower case, upper case, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
def getCountofRandomStrint(anystr):
    chars,digits,symbol=0,0,0
    for x in anystr:
        if x.isupper() | x.islower():
            chars +=1
        elif x.isnumeric():
            digits +=1
        else:
            symbol+=1
    print(f"Total counts of chars, digits and symbols are \n"
          f"Chars = {chars} \n"
          f"Digits = {digits} \n"
          f"Symbol = {symbol} \n")           


# In[240]:


getCountofRandomStrint(str1)


# In[246]:


#Given two strings, s1 and s2, create a mixed String
s1 = "Abc"
s2 = "Xyz"
exp = "AzbycX"
def mixString(s1,s2):
    s2 = s2[::-1]
    s1len= len(s1)
    s2len= len(s2)
    length = s1len if s1len > s2len else s2len
    newString=""
    for x in range(length):
        if (x < s1len):
            newString += s1[x]
        if (x < s2len):
            newString += s2[x]
    print(newString)
mixString(s1,s2)


# In[249]:


#Given an input string, count occurrences of all characters within a string
str1 = "Apple"
#exp {'A': 1, 'p': 2, 'l': 1, 'e': 1}
tempDict={}
for x in str1:
    cnt = str1.count(x)
    tempDict[x]=cnt
print(tempDict)

