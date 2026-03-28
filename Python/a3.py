#1
# ip=input("ENTER YOUR STRING :")
# new_ip=ip[::-1]
# if(ip==new_ip):
#     print("Given string is palindrome")
# else:
#     print("Given string is not palindrome")

#2
# list1=[1,2,3,4,5,6]
# sum=0
# for i in list1:
#     sum+=i

# print("average of the elements in the list is :",sum/len(list1))

#3
# list1=[]
# list2=[]
# for i in range(1,4):
#     num=int(input(f"In List 1 Enter number for index {i}:"))
#     list1.append(num)

# for i in range(1,4):
#     num=int(input(f"In list 2 Enter number for index {i}:"))
#     list2.append(num)

# print(list1)
# print(list2)
# list3=list1+list2
# print("new list is ",list3)
# list3.sort()
# print("sorted list:",list3)

#4
# tuple1=(1,2,3,4,5,6,7,8,9,10)
# tuple_even=tuple(i for i in tuple1 if i%2==0)
# tuple_odd=tuple(i for i in tuple1 if(i%2!=0))
# print("odd tuple:",tuple_odd)
# print("even tuple:",tuple_even)

#5
# student={}
# while True:
#     choice=input("Choose Option for particular operation: \n  Press A to add a student \n Press B to update marks \n  Press C to search for a student \n Press D to display all students and their marks \n Press Q to exit from program")
#     choice=choice.upper()
#     if(choice=='A'):
#         student_name=input("Enter Student Name:")
#         student_marks=int(input("Enter student marks:"))
#         student[student_name]=student_marks
#         print("ADDED SUCCESFULLY")
#     elif(choice=='B'):
#         name=input("Enter Student Name:")
#         marks=int(input("Enter student marks"))
#         student[name]=marks
#         print(f" for student {student[name]} marks updated succesfully")
#     elif(choice=='C'):
#         name=input("Enter student name you want to search : ")
#         if name in student:
#             print("Student found")
#         else:
#             print("Student not found")
#     elif(choice=='D'):
#         for name,marks in student.items():
#             print(name," : ",marks)
#     elif(choice=='Q'):
#         print("Exited Program Succesfully")
#         break
#     else:
#         print("Invalid Operation")
                
#6
# words =["apple","banana","kiwi","cherry","mango"]
# dict1 = {}
# for i in words:
#     dict1[i]=len(i)
# print(dict1)

#7
# ip=input("Enter a string with spaces:")
# space_count=0
# for i in ip:
#     if(i==' '):
#         space_count+=1
    
# print("Total spaces in given string is :",space_count)

#8
# list1=[1,2,3,4,5]
# list2=[2,324,21]
# set1=set(list1)
# set2=set(list2)
# common_element = set1.intersection(set2)

# if common_element:
#     print(f"Common element is present which is {common_element}")
# else:
#     print("no common element is present")

#9
# list1=[1,1,2,2,3,4,5,6,6]
# set1=set()
# for i in list1:
#     if(list1.count(i)>1):
#         set1.add(i)

# print("Repeating elements : ",set1)

#10
# str1 = input("Enter a string: ")

# unique = []
# for ch in str1:
#     if ch not in unique:
#         unique.append(ch)

# print("Unique characters:", unique)
# print("Count:", len(unique))