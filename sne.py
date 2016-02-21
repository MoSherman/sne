# A script which takes a list of names and assigns them to each other but never to themselves
# The goal is to also export the name to a .txt file named after the person and within the person they received

import csv # importing csv module
import sys #importing sys module for .txt creation
import os  # Import os


path  = os.path.expanduser('~/Projects/sne/names.csv') # Specifying path to names emails
names = csv.reader(file(path)) # Creating a list of the names and emails                                       

# Assign login details to connection variables
for i in names:
    name    = i[0]
    email   = i[1]
    
    print name + ": " + email



#def name_file():                        # Function for creating new .txt name files
    #file_name = 
