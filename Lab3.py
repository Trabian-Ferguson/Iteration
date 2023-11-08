# Program Name: Lab3.py
# Course: IT1114/Section 01
# Student Name: Trabian Ferguson
# Assignment Number: Lab3
# Due Date: 09/10/2023
# Purpose: This program allows a manager to deterine and display the total sales for the department. 

#sales goal input for manager
sg = input("Sales goal: ")
sg = float(sg)

# count to keep count of salespeople
count = 1


sum = 0.0

answer = "y"

while answer == "y":
    for i in range(1,5):
        x = float(input("Salesperson "+ str(count) + " week " + str(i)+ ":"))
        sum = sum + x
    answer = input("Another salesperson?")
    count = count + 1
                     
mgrbonus = 0
                     
if sum > sg:
    mgrbonus= sum *.05
else:
    mgrbonus= sum* .02

                     
print("Department Monthly Sales and Commission")
print()
print("Number of Employees: " + str(count-1))
print("Department Sales Goal:$" + str(sg))
print("Total Sales: $"+ str(sum))
print("Mgr. Bonus: $" + str(mgrbonus))
                    
