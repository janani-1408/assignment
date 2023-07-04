#Programs on selection and iteration
print("Program to find odd or even if it is odd find the factorial otherwise check whether it is palindrome or not")
num=int(input("Enter the number:"))
fact=1
if(num%2==1):
    for i in range(1,num+1):
        fact=fact*i
    fact_str=str(fact)        
    num_digits=len(fact_str)
    print("The factorial of a given number is ",fact)
    print("The number of digits in factorial number :",num_digits)

        
else:
    num_str=str(num)
    reversed_str=num_str[::-1]
    if(num_str==reversed_str):
        print("The given number is palindrome")
    else:
        print("The given number is not a palindrome")

#Strings and its operations
print("Substring or not")
str1=input("Enter the string1:")
str2=input("Enter the string2:")
if(len(str1)<len(str2)):
    print("No")
else: 
    i=0
    j=0
    while i<len(str1) and j<len(str2):
        if str1[i]==str2[j]:
            j+=1
        i+=1

    if(j==len(str2)):
        print("Yes")
    else:
        print("No")

#Lists and its operations
#(a)
print("Positive and negative indexing")
lst=list(input("Enter the list elements:").split())
print(lst)
print("Positive indexing")
for i in range(0,len(lst)):
    print("list[",i,"]:",lst[i])
print("Negative indexing")
for i in range(-len(lst),0):
    print("list[",i,"]:",lst[i])

#(b)
print("Ascending order or not")
lst=list(input("Enter the list elements:").split())
print(lst)
lst1=lst[:]
lst1.sort()
if lst==lst1:
    print("Yes,it is a ascending order")
else:
    print("No,it is not a ascending order")

#Tuples and its operations
#(a)
print("To convert tuple into string")
tupl=tuple(input("Enter the input:").split())
print(tupl)
str1=''
for i in tupl:
    str1+=i
print("String is",str1)

#(b)
print("To reverse a tuple")
tupl=tuple(input("Enter the input:").split())
print("The orginal tuple :",tupl)
print("The reversed tuple :",tupl[::-1])

#Sets and its operations
print("to check subset or not")
set1=set(input("Enter the elements:").split())
set2=set(input("Enter the elements:").split())
print("Set 1:",set1)
print("Set 2:",set2)
ans=set2.issubset(set1)
if ans==True:
    print("Yes,it is a subset")
else:
    print("No,it is not a subset")

#Dictionaries and its operations
print("To iterate over dictionaries using for loop")
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

for key, value in my_dict.items():
    print(key, value)

