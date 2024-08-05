# -*- coding: utf-8 -*-
"""
@author: Jaishevanth
"""

# importing the module
import sys
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def initial_phonebook():
    df = pd.read_excel(r'contact book.xlsx')
    vals = df.values
    return vals


def menu():
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Search for a contact")
    print("4. Exit phonebook")

    choice = int(input("Please enter your choice: "))

    return choice


def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(
                str(input("Enter category(Family/Friends/Work/Others): ")))
    pb.append(dip)

    print("Contact added successfully")
    
    return pb


def remove_existing(pb):
    query = str(
        input("Please enter the name of the contact you wish to remove: "))

    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1

            print(pb.pop(i))

            print("This query has now been removed")

            return pb
    if temp == 0:
        print("Sorry, you have entered an invalid query.\
	Please recheck and try again later.")

        return pb

def search_existing(pb):
    choice = int(input("\n\n1. Name\n2. Number\n3. Email-id\n4. DOB\nEnter search criteria : "))
    temp = []
    check = -1

    if choice == 1:
        query = str(
            input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice == 2:
        query = int(
            input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])

    elif choice == 3:
        # This will execute for searches based on contact's e-mail address
        query = str(input("Please enter the e-mail ID\
		of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])

    elif choice == 4:
        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY)\
			of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])

    else:
        print("Invalid search criteria")
        return -1

    if check == -1:
        return -1

    else:
        for i in range(len(temp)):
            print("Record ", i+1, "\nName \t\t: ", temp[i][0], "\nNumber \t\t: ", temp[i][1], "\nEmail \t\t: ", temp[i][2], "\nD.O.B. \t\t: ", temp[i][3])
        return check


def thanks(pb):
    df = pd.DataFrame(pb, columns=['Name', 'Number', 'Email', 'Category'], dtype=float)

    df.to_excel("contact book.xlsx", index=False)
    print("Thank you")


ch = 1

pb1 = initial_phonebook()

pb = list(pb1)
while ch in (1, 2, 3):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        d = search_existing(pb)
        if d == -1:
            print("The command does not exist. Please try again")
    else:
        thanks(pb)
