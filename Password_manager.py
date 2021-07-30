import pickle
import random
import os
import tkinter

MasterKeyList = []
UserRecordsList = []

# Specifying paths for source files

fileIn1 = "MasterRecords.txt"
fileOut1 = "MasterRecords.txt"

fileIn2 = "UserRecords.txt"
fileOut2 = "UserRecords.txt"


######################################################################################################################################

# defining all necessary variables

def AddAccount(UserRecords):
    with open(fileOut2, "wb") as file:
        pickle.dump((UserRecords), (file))


def EditAccount(UserRecords):
    for i in range(len(UserRecords)):
        if records[i][0] == AccountName:
            records[i] = newRecord
        break
    return records


def FindAccount(UserRecords):
    AccountName = input("Enter the name of the account you wish to search for e.g reddit")

    for i in range(len(records)):
        if UserRecords[i][1].lower() == AccountName:
            return UserRecords[i]


def DeleteAccount(UserRecords):
    for i in range(len(UserRecords)):
        if UserRecords[i][0] == AccountName:
            del UserRecords[i]
            break

    return UserRecords


def CreateMasterKey(NewKey):
    with open(fileOut1, "wb") as file:
        pickle.dump((NewKey), (file))


def GetMasterKey(MasterRecords):
    MasterKey


######################################################################################################################################

# First menu

# Login stage
def login():
    attempts = 3

    choosing = True
    while choosing:
        choice = int(input("1)Login\n2)Register\n3)Quit\n> "))

        # login
        if choice == 1:
            for cd in reversed(range(attempts)):
                MasterKey = input("Enter your master key to continue:")
                if input("Enter your master key to continue:") == MasterKey():
                    return True
                else:
                    print("Incorrect, {} attempts remaining..".format(cd))
            return False

        # Registration stage
        elif choice == 2:
            if choice == 2:
                print("Welcome to SmartPass please create your master key,")
                print("this key will be required the next time you login")
                print("please take not of this key as you will be unable to recover it if lost.")
                print("")
                print("")
            MasterKey = input("Enter your master Key:")
            print("Your master key has been successfully created!")
            CreateMasterKey(NewKey)
            LoggedIn = True
            choosing = False

        # Quit option
        elif choice == 3:
            print("Thank you for using SmartPass, bye now")
            os.exit(3)

        else:
            print("Invalid input, please try again")


def main():
    if login():
        print("You are currently logged in to SmartPass")
        loggedIn = True

        while LoggedIn:
            choice = int(input(
                "1)Add account\n2)Edit\n3)Display all accounts\n4)Find account\n5)Delete account\n6)Generate random password\n7)Logout\n> "))

        # Add Account option
        if choice == 1:
            account = "stuff"
            AddAccount(UserRecords)

        # Edit Account option
        elif choice == 2:
            input("Enter the name of the account you wish to edit:")
            EditAccount(UserRecords)

        # View all accounts/records
        elif choice == 3:
            DisplayAccounts(UserRecords)

        # Find Account
        elif choice == 4:
            print("Enter the name of the account you would like to find e.g facebook")
            FindAccount(UserRecords)

        # Delete Account
        elif choice == 5:
            DeleteAccount(UserRecords)

        # Generate random password option
        elif choice == 6:
            alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#!$&(@3187%=+}{<->?"
        pw_length = 15
        mypw = ""

        for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

        print(mypw)

        # Logout and quit program
        if choice == 7:
            LoggedIn = False
            print("Logging out of your session....")

        else:
            print("You are now logged out, bye!")


if __name__ == "__main__":
    main()