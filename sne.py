# A script which takes a list of names and assigns them to each other but never to themselves
# The goal is to also export the name to a .txt file named after the person and within the person they received

import csv # importing csv module
import sys #importing sys module for .txt creation
import os  # Import os
import random


path  = os.path.expanduser('~/Projects/sne/names.csv') # Specifying path to names emails
names = csv.reader(file(path)) # Creating a list of the names and emails  
names2 = csv.reader(file(path)) # Creating a duplicate of the list

receivers = []
givers = []

#creating receivers list in a random order
for i in names2:
    
    name = i[0]
    receivers.append(name)
    
random.shuffle(receivers,random.random)

#creating givers list in order that was given with emails
for i in names:
    
    name = i[0]
    email = i[1]
    givers.append([name,email])
    #combi = name + ',' + email
    #givers = [[name,email]]        
    #givers = [name,email]
    #givers.append(name)
    #givers.append(email)

#print givers[0][0]

for i in receivers:
    receiver = i
    #print receiver + "R"
    for i in givers:
        giver = i[0]
        if giver != receiver:
            print str(giver) + "g, " + str(receiver) + "r end"
        #giver = i[0]
        #email2 = i[1]
        #print giver + "G"
        #if receiver != giver:
            #receivers.remove(receiver)
            #target = open(giver, 'w')
            #text = "You got " + str(receiver) + " in the Secret Name Exchange! Your email is: " + str(email2)
            #target.write(text)
            #target.close
        #elif receiver == giver:
            #for i in receivers:
                #receiver = i[4][0]
        #else:
            #print "That doesn't seem to have worked!"
    









#for i in names:
    
    #giver = i[0]
    #email = i[1]
    #name =random.choice(names2)
    
    #if giver != name:
        
        #names2.remove(name)
        #target = open(giver, 'w')
        #text = "You got " + name + " in the Secret Name Exchange! Your email is: " + email
        #target.write(text)
        #target.close
    
    #elif giver == name:
        
        #name = random.choice(names2)
    
    #else:
        
        #print "That doesn't seem to have worked!"



#for i in names2:
    #name = random.choice(names2)
    #names2.remove(name)
    
    #for i in names:
        #giver = i[0]
        #email = i[1]
        
        #if giver != name:
            #names2.remove(name)
            #target   = open(giver, 'w')
            #text     = "You got " + name + " in the Secret Name Exchange! Your email is: " + email
            #target.write(text)
            #target.close
        
        #elif giver == name:
            
            #for i in names2:
                #name = random.choice(names2)
        
        #else:
            #print "That doesn't seem to have worked..."


#for i in names:
    #giver    = i[0]
    #email    = i[1]
    #reciever = random.choice
    #target   = open(giver, 'w')
    #text     = "You got " + receiver + " in the Secret Name Exchange! Your email is: " + email
    #target.write(text)
    #target.close



#def name_file():                        # Function for creating new .txt name files
    #file_name = 
