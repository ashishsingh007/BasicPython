#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Flow to read a file in python is 
1) Open the file
2) read or write the file
3) close the file

Mode	Description
r	Opens a file for reading. (default)
w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Opens a file for exclusive creation. If the file already exists, the operation fails.
a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Opens in text mode. (default)
b	Opens in binary mode.
+	Opens a file for updating (reading and writing)
'''


# In[17]:


try:
    openFile = open('F:/DummyTest.txt',mode='r')
    #print(openFile)
    print(openFile.read())
except 
finally:
    openFile.close()


# In[38]:


try:
    f = open('F:/DummyTest_1.txt',mode='r')
    print(f.read())
except FileNotFoundError as e:
    print(e.strerror ,'-' , e.filename)

