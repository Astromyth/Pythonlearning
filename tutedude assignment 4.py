#Assignmnet 4 - Module 5: Files, Exceptions, and Errors in Python
#Task 1: Read a File and Handle Errors

'''
try:                                         #4 enclosed entire reading in try so both execution can be done in one go
    file =open("sample.txt","r")             #1 this will open file in read mode
    my_file =file.read()                     #2 this will read the file line by line
    print(my_file)                           #3 it will print files line by line
    file.close()

except FileNotFoundError:                   # 5 in case file itself is not present it will throw error
    print("Error: The file 'sample.text' was not found .")

'''



#Task 2  Write and Append Data to a File
user_data = input("Enter the text to the file:")             #1 this take input first
Original_file =open('output.text','w')                       #2 this open file with write permission
writing_file = Original_file.write(user_data)                #3 write user inserted data  in file
print('Data successfully Updated output.text')              #4closing this open file
Original_file.close()


Original_file =open('output.text','a')                       # we open file again
user_data=input("Enter the additional Text to append:")       #6 ask user data again
apending_file=Original_file.write("\n" + user_data)           #7 create apending file with new user data with new line
Original_file.close()                                        #8 closing file again

Original_file = open('output.text', 'r')                   #9 opening file with read permission
my_file = Original_file.read()                              #read the data
print('Final content of output.text:'+'\n'+my_file)         #11 printing all line in file
Original_file.close()