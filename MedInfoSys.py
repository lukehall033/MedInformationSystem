#!/usr/bin/env python3

#Mock medical information system application

import os, sys
import time
import shutil

os.system("clear")
print("""

##################################
#      ___  __   ____   ______   #
#     /   \/  \  |  |   \  __/   #
#    /  _   _  \ |  | __/  \     #
#   /__/ \_/ \__\|__|/_____/     #
#   Medical Information System   #
#   Luke Hall | v 1.0            #
#                                #
##################################

[+] View Records
[-] Enter Records
[=] Search Records
[>] Delete Records
[*] Edit Records
[0] Close System
""")

def view_records():
    cont = "Y"
    while (cont == "Y"):
        os.system("clear")
        print("""
################################
        
          Patient List

################################
        """)
        directory = os.scandir("/home/lukeh/PythonProjects/MedRecords")
        print()
        for entry in directory:
            print(entry.name.replace(".dat", ""))
        print()

        record = input("Select Which Record to View: ")
        os.system("less /home/lukeh/PythonProjects/MedRecords/" 
                  + record + ".dat")
        print()
        cont = input("View Another Record? (Y/N): ")
    
        if (cont == "N"):
            python = sys.executable
            os.execl(python, python, * sys.argv)

def enter_records():
    val = "Y"
    while (val == "Y"):
        os.system("clear")
        print("""
################################
        
     Enter New Patient Info

################################

        """)
        name = input("Name (Last, First, MI): ") 
        print()
        dob = input("Date of Birth (MM/DD/YYYY): ")
        print()
        sex = input("Sex (M/F): ")
        print()
        address = input("Address: ")
        print()
        phone = input("Phone Number: ")
        print()
        insurance = input("Insurance: ")
        print()
        Rx = input("Current Perscriptions: ")
        print()
        conditions = input("Major Health Conditions: ")
        print()
        comments = input("Additional Comments: ")
        print("\nAdding new patient to system...\n")
        bar = ["[", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "]"]

        for i in range(len(bar)-2):
            bar[i+1] = "#"
            print("".join(bar), end="\r")
            time.sleep(0.2)
        print("".join(bar) + " Patient Added!")

        file_name = name.replace(",", "").replace(" ", "") + ".dat"
        dat_file = open(file_name, "w")
        dat_file.write("Name: " + name)
        dat_file.write("\nDOB: " + dob)
        dat_file.write("\nSex: " + sex)
        dat_file.write("\nAddress: " + address)
        dat_file.write("\nPhone: " + phone)
        dat_file.write("\nInsurance: " + insurance)
        dat_file.write("\nPerscriptions: " + Rx)
        dat_file.write("\nConditions: " + conditions)
        dat_file.write("\nComments: " + comments)
        dat_file.close()
        shutil.move("/home/lukeh/PythonProjects/" + file_name,
                    "/home/lukeh/PythonProjects/MedRecords")

        cont = input("\nEnter Another Patient? (Y/N): ")
        if cont == "N":
            python = sys.executable
            os.execl(python, python, * sys.argv)
        else:
            var = cont

def search_records():
    cont = "Y"
    while (cont == "Y"):
        matches = []
        os.system("clear")
        print("""
################################
        
         Search Records

################################
        """)
        search = input("What Information to Search by? (DOB, Name, Condition): ")
        inpt = input("\nSearching by " + search + ", Enter Input: ")
    
        records = os.scandir("/home/lukeh/PythonProjects/MedRecords")
        for entry in records:
            fle = open("/home/lukeh/PythonProjects/MedRecords/" 
                       + entry.name, "r")
            if (search == "Name"):
                line = fle.readline().strip("\n")
                if (line == ("Name: " + inpt)):
                    matches.append(entry.name.strip(".dat"))
            elif (search == "DOB"):
                line = fle.readlines()[1].strip("\n")
                if (line == "DOB: " + inpt):
                    matches.append(entry.name.strip(".dat"))
            else:
                line = fle.readlines()[7].strip("\n")
                if (line == "Conditions: " + inpt):
                    matches.append(entry.name.strip(".dat"))
            fle.close()
        
        print()
        for i in range(len(matches)):
            print(matches[i])
            print()

        cont = input("Search for Another Record? (Y/N): ")
        if (cont == "N"):
            python = sys.executable
            os.execl(python, python, * sys.argv)

def delete_records():
    val = "N"
    while (val == "N"):
        os.system("clear")
        print("""
################################
        
          Patient List

################################
             """)
        directory = os.scandir("/home/lukeh/PythonProjects/MedRecords")
        print()
        for entry in directory:
            print(entry.name.replace(".dat", ""))
        print()

        del_file = input("Which Record Should be Deleted: ")
        os.remove("/home/lukeh/PythonProjects/MedRecords/" + del_file + ".dat")
        val = input("Record Deleted! Exit? (Y/N): ")

        if val == "Y":
            python = sys.executable
            os.execl(python, python, * sys.argv)

def edit_records():
    cont = "Y"
    while (cont == "Y"):
        file_list = []
        os.system("clear")
        print("""
################################
        
          Patient List

################################
        """)
        directory = os.scandir("/home/lukeh/PythonProjects/MedRecords")
        print()
        for entry in directory:
            file_list.append(entry.name.replace(".dat", ""))
            print(entry.name.replace(".dat", ""))
        print()

        print("(In editor, press 'i' to start editing," +
              " 'esc' -> ':' -> 'wq' to exit)")
        record = input("Select Which Record to Edit: ")
        if record in file_list:
            os.system("vi /home/lukeh/PythonProjects/MedRecords/" 
                      + record + ".dat")
            cont = input("\nEdit Another Record? (Y/N): ")
        else:
            print("\nNo Record Found")
            time.sleep(1)
        if (cont == "N"):
            python = sys.executable
            os.execl(python, python, * sys.argv)

def close_system():
    os.system("clear")
    sys.exit()

operation = input("Enter the symbol for which action you'd like to perform: ")

process_dict = {"+": view_records,
                "-": enter_records,
                "=": search_records,
                ">": delete_records,
                "*": edit_records,
                "0": close_system}

process_dict[operation]()
