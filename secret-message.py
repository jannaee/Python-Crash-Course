import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\Jannaee\Desktop\~GitProjects\Python-Crash-Course\secret-message-pics\new")
    #(2) change working directory - mind the double backslash
    os.chdir(r"C:\Users\Jannaee\Desktop\~GitProjects\Python-Crash-Course\secret-message-pics\new")
    #(3) loop over the filename list and rename each
    for file_name in file_list:
        table = str.maketrans(dict.fromkeys('0123456789'))
        os.rename(file_name,file_name.translate(table))    
rename_files()
