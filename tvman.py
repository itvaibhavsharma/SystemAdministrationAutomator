import random
import os
import sys
import csv
class User:
    database = "UserDatabase.csv"
    requirePassword = True
    maxUsers = 1000 #not used
    usersList = []
    myData = []
    def __init__(self, name, id_num, DOB,user_type="Normal"):
        self.name = name
        self.id_num = int(id_num)
        self.DOB = DOB
        self.user_type= user_type
        self.usersList.append(self)
    def showObjectProperties():
        print("\nCurrent Objects in class: ")
        print("-------------------------")
        for j in range(0,len(User.usersList)):
            print(User.usersList[j].name)
            print(User.usersList[j].id_num)
            print(User.usersList[j].DOB, "\n")
    def checkId_num(newNumber):
        for k in range(0,len(User.usersList)):
            if(User.usersList[k].id_num == newNumber ):
                return False
        return True
    def showUsers():
        print("\nThere are currently", len(User.usersList), "users subscribed....")
        for user in User.usersList:
            print("--------------")
            print("INFO || Name:",user.name,end='')
            print("\t|| User ID:",user.id_num,end='')
            print("\t|| DOB:",user.DOB)
    def addUser():
        newUser = User(input("please enter a name: "),(
                  getUniqueNumber()), (
                  str(grabDate())) )        
        print("\nNew user added...\n")
    def loadUsers():
        print("\n\n\nLoading users from database file: ", User.database)
        print("\n\n")
        myFile = open(User.database, 'r')        
        with myFile:
            data = list(csv.reader(myFile))
            for entry in data:
                newuser = User(entry[0], entry[1], entry[2]) #<------ use this method
    def saveUsers():
        tosave = []
        for i in range(0, len(User.usersList)):
            data = [User.usersList[i].name,
                         User.usersList[i].id_num,
                         User.usersList[i].DOB ]
            tosave.append(data)
        print("\n\nData Converted.....\n\n")
        myFile = open(User.database, 'w', newline='')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(tosave)
        print("\nDatabase saved....\n")
    def nameCompare(selector, username):
        selector = selector.lower()
        username = username.lower()
        sel = selector[0:selector.find(" ")]
        sel=sel.replace(" ","")
        ector = selector[selector.find(" ")+1:]
        ector=ector.replace(" ","")
        if( selector == username):
            return True
        elif( (username.find( sel ) != -1) or (username.find( ector ) != -1) ):
            return True
        elif( (username.find( sel[:3] ) != -1) or (username.find( ector[:3] ) != -1) ):
             return True 
        if( selector == username):
            return True
        elif( (username.find( sel ) != -1) or (username.find( ector ) != -1) ):
            return True
        elif( (username.find( sel[:3] ) != -1) or (username.find( ector[:3] ) != -1) ):
             return True 
    def delUser(selector):   
        matches=[]
        if(num_there(selector) ):
            print("\nNumber Found!!\nID Number or Date....\n\n")
            if( (len(selector) == 8) and (selector[2] == "/") ):
                print("\n\n*Date identifier entered")

                for k in range(0,len(User.usersList)):
                    if(User.usersList[k].DOB == selector ):
                        print("DOB match found at item # ", k)
                        matches.append(k)
            else:
            
                print("\nID Number entered.....")
                for k in range(0,len(User.usersList)):
                    if( str(User.usersList[k].id_num) == selector ):
                        print("ID Number match found at item # ", k)
                        matches.append(k)
        else:
            print("No Number!!\nname identifier")
            for k in range(0,len(User.usersList)):
                if( User.nameCompare( selector, User.usersList[k].name ) ):
                    matches.append(k)
        if( len(matches) == 1 ):
            print("\nOne possible match found\n")
            print("\nMatch Name: \n",User.usersList[matches[0]].name,"\n")
            toRemove=input("\nWould you like to delete a user? [Y/N]\n")
            try:
               val = int(toRemove)
            except ValueError:     
                print("\n\nPlease enter a valid integer user index to delete...")
                return
            if( toRemove.lower() == "y" ):
                print("Deleting User")
                User.usersList.remove(User.usersList[ matches[0] ])

            else:
                print("\nContinuing without deletion....")
            
        elif( len(matches) > 1):
            print("\n\n\nMultiple matches found!\n\nPrinting matches:")
            for match in matches:
                print(User.usersList[match].name)
            toRemove = input("""\n\nWould you like to delete a user?
                             If yes, enter which user
                             ----------------------
                             1 - First Match Shown
                             2 - Second Match Shown
                             n - nth match....\n""")
            try:
               val = int(toRemove)
            except ValueError:     
                print("\n\nPlease enter a valid integer user index to delete...")
                return
            
            print("\nYou have selected item number",toRemove,"to remove\n") 
            print("\nDeleting user number",toRemove,"with name",selector,"\n")
            print("This will delete user #",matches[int(toRemove)-1],"from master list")
            User.usersList.remove(User.usersList[matches[int(toRemove)-1]]) #the second match will really be @ index n-1 in array
            print("\nUser Deleted....\n")
            print("\nDo Nothing...")

    def deleteUser(selector):
        matches=[]
  
        if(num_there(selector)):
           print("\n\n*Number identified in the selector\n")
           if( (len(selector) > 2) and (selector[2] == "/") ):
               print("\n\n*Date identifier entered")
               if(len(selector) == 8):
                   print("Correct Date Format entered")
                   for k in range(0,len(User.usersList)):
                       if(User.usersList[k].DOB == selector ):
                           print("DOB match found at item # ", k)
                           print("Deleting user with DOB: ", selector)
                           User.usersList.remove(User.usersList[k])
               else:
                   print("Incorrect Date Format....")
                   
                   
           else:
               print("\n*ID Number identifier entered")
               for k in range(0,len(User.usersList)):
                   if(User.usersList[k].id_num == int(selector) ):
                       #found id number match
                       print("ID Number match found at item # ", k)
                       print("Deleting user with id number: ", selector)
                       User.usersList.remove( User.usersList[k] )
                       return
               print("\n\nNo matching ID number found in database.....\n\nReturning to program....\n")



        else:
            print("\n\nName identifier entered")
            selector=selector.lower()
            for k in range(0,len(User.usersList)):
                if(User.usersList[k].name.lower() == selector ):
                    print("\nExact name match found!\nMatch at index: ",k)
                    matches.append(k)            
            if( len(matches) > 0):
                print("\n\n\nPerfect matches found!\n\nPrinting matches:")
                for match in matches:
                    print(User.usersList[match].name)
                toRemove = input("""\n\nWould you like to delete a user?
                                 If yes, enter which user
                                 ----------------------
                                 1 - First Match Shown
                                 2 - Second Match Shown
                                 n - nth match....\n""")
                print("\nYou have selected item number",toRemove,"to remove\n") 
                print("\nDeleting user number",toRemove,"with name",selector,"\n")
                print("This will delete user #",matches[int(toRemove)-1],"from master list")
                User.usersList.remove( User.usersList[ matches[int(toRemove)-1] ])
                print("\nUser Deleted....\n")                
            else:
                print("\nNo perfect name match found!")
                if(selector.find(" ") != -1):
                    print("\nFirst and last name entered..")
                    sel = selector[0:selector.find(" ")]
                    ector = selector[selector.find(" ")+1:]
                    print("""\nNo user found with exact name match.
                          Selector entered with a first and last name.""")
                    print("After splitting the selector, \nsel = ",sel,"\nector = ",ector,"\n")
                    print("------------------------------------------------$$")
                    print("\nChecking the list of users for possible matches..")
                    for k in range(0,len(User.usersList)):                   
                        first = User.usersList[k].name[0:User.usersList[k].name.find(" ")]
                        last = User.usersList[k].name[User.usersList[k].name.find(" "):]
                        first = first.replace(" ","").lower()
                        last = last.replace(" ","").lower()
                        if( first == sel):
                            matches.append(k)
                        elif(last == ector):
                            matches.append(k)
                    if( len(matches) > 0):
                        print("\n\nNo direct matches, here are some similar results:\n")
                        for match in matches:
                            print(User.usersList[match].name)
                        toRemove = input("""\nWould you like to delete a user?
                                         If yes, enter which user
                                         ----------------------
                                          0 - Delete No Matches
                                          1 - First Match Shown
                                          2 - Second Match Shown
                                          n - nth match....\n""")
                        try:
                           val = int(toRemove)
                        except ValueError:     
                            print("\n\nPlease enter a valid integer user index to delete...")
                            return
                        if( int(toRemove)-1 < len(matches) and (matches[int(toRemove)-1] < len(User.usersList)) ):
                            print("\n\nDeleting User: ",User.usersList[int(toRemove)]) #make sure its in range
                        else:
                            print("\n\n\nNumber outside range.\nExiting....\n\n\n")
                            return
                        if( toRemove == "0" ):
                            print("\nDeleting no matches and continuing..\n\n")   
                        else:
                            User.usersList.remove( User.usersList[ matches[int(toRemove)-1] ])
                            print("\n\nUserDeleted...\n\n")
                    else:
                        print("\nNo near matches found...")
                else:
                    print("\nPlease enter a first and last name\n\n")
    def showUserByPosition(position):
        print(User.usersList[position].name)
        print(User.usersList[position].id_num)
        print(User.usersList[position].DOB,"\n")
    def showUserByNameDate(identifier):    
        if( type(identifier) == str):
            print("String identifier")
            print("Please enter a name or date:")
            if( (len(identifier) > 3) and (identifier[2] == '/')):
                print("Date identifier")
                for j in range(0,len(User.usersList)):
                    if( User.usersList[j].DOB == identifier):
                        print("\nDate match found!!")
                        User.showUserByPosition(j) #this is better version
                        return
                print("\nNo match found....")
            else:
                print("Name identifier")
                for j in range(0,len(User.usersList)):
                    if( User.usersList[j].name.lower() == identifier.lower()):
                        print("\nName match found!!")
                        User.showUserByPosition(j)
                        return
                print("\nNo match found....")
                
        
    def showUserPosition(self):
        return True
    def showName(identifier):
        print(User.usersList[identifier].name)
def getUniqueNumber():
    unique = False 
    while(not unique): 
        num = random.randrange(1,User.maxUsers)   
        if(User.checkId_num(num) == True):
            unique = True   
    return num
def grabDate():
    while(True):
        date = input("Please enter a user's DOB: [mm/dd/yy] ")
        if( len(date) == 8 and date[2] == "/"):
            return date
        else:
            print("Incorrect date format!\nEnter date as: [mm/dd/yy] ")
def deleteUser():
    print("\nDeleting user...")
    selector = input("Please enter a name, ID number, or date: ")
    User.delUser(selector)
        
def num_there(s):
    return any(i.isdigit() for i in s)

def loadDatabase():
    User.loadUsers()
def save_database():
    print("\nSaving Database....\n")
    User.saveUsers()
    return 1
def determineState():
    save=input("\nWould you like to save the database before closing? [Y/N]\n")
    if( save.lower() == "y" ):
        print("\nSaving database and exiting....\n")
        save_database()
    else:
        print("\nQutting program without saving....\n")        
    return 1
def display_home_message():
    print("\nHello! Welcome to the Electric management system.....")
    s = input("""Select the Option
          1 - Registered Users
          2 - Add a New User
          3 - Delete User
          4 - Show a User
          5 - Save Database
          6 - More Options
          7 - Quit\nWaiting...\nSelect one value:""")
    return s
loadDatabase()
while( True ):
    os.system("clear")
    print("----------------------------------")
    s=display_home_message()
    print("**The value chosen is: ",s)
    if(s == "1"):
        User.showUsers()
        input("Press Enter to  continue")
    elif(s == "2"):
        User.addUser()
        input("Press Enter to  continue")
    elif(s == "3"):
        deleteUser()
        input("Press Enter to  continue")
    elif(s == "4"):    
        print("'Show a User' selected")
        User.showUserByNameDate(input("Please enter a name or date identifier: "))
        input("Press Enter to  continue")
    elif(s == "5"):
        save_database()
        input("Press Enter to  continue")      
    elif(s == "6"):
        print("\n\nYou have selected more option.\nThere are none at the moment \n;)\n")
        input("Press Enter to  continue")
    elif(s == "7"):
        print("Quitting Program....")
        determineState()
        sys.exit(0)
    else:
        print("Please enter a valid key...")
        input("Press Enter to  continue")
    print("\n\n")
