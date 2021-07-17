# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:35:35 2021

@author: lhrle
"""

    # Initialize variables
phonebook = []
list1 = []
var_b = True

    # Instructions message
print("Welcome \n")
print("Press A to add a contact \n"
      "Press S to search for a contact \n"
      "Press E to exit the system"
      )

    # Accept the user´s input
while var_b:
    var_fun = input("What function do you want to perform?")
    
        # Option "A"
    if var_fun == "A":
        list1 = []
        list1.append(input("Enter contact name: "))
        list1.append(input("Enter phone number: "))
        list1.append(input("Enter contact email: "))
        phonebook.append(list1)
        print("The directory has been updated")
    
        # Option "S"
    if var_fun == "S":
        var_bs = False
        var_s = input("Contact to search: ")
        for x in phonebook:
            if var_s in x[0]:
                var_bs = True
        if var_bs == True:
            print("The contcact is in the phonebook")
        else:
            print("The contcact isn´t in the phonebook")
        
        # Option "E"
    if var_fun == "E":
        print("Exiting the system")
        var_b = False
        
        