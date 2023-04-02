#file operations in file handling
f = open('firstfile','w')
f.write("hello this himani")#write operation
f.close()
f = open('firstfile','a')
f.write(" ""sharma")#append function
f.close()
f = open('firstfile','r')
print(f.read(8))#read function
f.close()