import os

def rename_files():
    #1 get file names from a folder
    fileslist = os.listdir(r"C:\Users\Jannaee\Desktop\~GitProjects\Python-Crash-Course\secret-message-pics\new")
    print (fileslist)# r is placed in front of the string becuase it tells python not to interpret the string in any other way but to take it as it is
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\Jannaee\Desktop\~GitProjects\Python-Crash-Course\secret-message-pics\new")
    #2 remame each file
    for file_name in fileslist:
        translation_table = str.maketrans("0123456789","          ","0123456789")
        os.rename(file_name, fileslist.translate(translation_table))
    os.chdir(saved_path)

rename_files()
