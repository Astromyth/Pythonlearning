#ASSIGNMENT 5:  Module 6: Data Structures and Strings in Python
# Task 1: Create a Dictionary of Student Marks

Student_List={'alice':'95','mark':'75','richard':'65'}                 #created List

Q=str(input('Enter the student name:'))                                # defined Input with string value

Q_lower=Q.lower()                                                      # handled Integrity issues like case issues

if Q_lower in Student_List:
    print(f'{Q} marks is :',Student_List[Q_lower])

else:
    print("Student not found")


# Task 2    Task 2: Demonstrate List Slicing
List_Name = list(range(1,11))                                  # create range
print("orignal_List",List_Name)                                # printing details as initial
print("Extracted first five element:",List_Name[0:5])          # sliced first five numbers
print("Reversed Extracted  five element:",list(reversed(List_Name[0:5])))         # instead of creating multiple variable j
