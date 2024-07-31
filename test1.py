import os

# Vars ..................................................
path = input("Enter the path: ")
folder_name = input("Enter project name: ")
workpath = "c:\\" + folder_name + "\\"

#
def Create_Project(folder_name):
    if os.path.isdir("c:\\" + folder_name):
        print("The folder '" + folder_name + "' already exist.")
    else:
        os.system("mkdir " + "c:\\" + folder_name)
        print("The folder '" + folder_name + "' created in the path: c:\\" + folder_name)
def Dir_Master_Path():
    os.system("dir " + path + " > " + workpath + folder_name + ".txt")
def Get_total_size():
    option = input("Wanna get full project size now (Y), Never (N), Skip it now(S): ")
    if option == "y" or "Y":
        print("Calculating of the total project size in processing . . .")
        os.system("dir /s " + path + " > " + workpath + "total_size.txt")
        print("Total size of the project calculated into '" + workpath + "total_size.txt'")
    elif option == "n" or "N":
        print("--")
    elif option == "s" or "S":
        print("The total size calculation option will skip for now.")

# Working area ..................................................
# Create_Project(folder_name)
# Dir_Master_Path()
Get_total_size()

