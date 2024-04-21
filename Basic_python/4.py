import os
path = ""
# if os.path.exists(path) # checking if the path exist
# if os.path.isfile(path)
# if os.path.isdir(path)

with open("D:\Rajeeb\dreams\projects\python_mastery\Basic_python\plain_text.txt") as file: # with open closes file automatically other wise we have to file.close()
    print(file.read())


try:
    with open("text.txt") as file: # with open closes file automatically other wise we have to file.close()
        print(file.read())
except FileNotFoundError as e:
    print(e)

with open("text.txt",'w') as file: # overwrite the original as 'w'
    file.write("My name is John cena") 

with open("text.txt",'a') as file: # overwrite the original as 'a'
    file.write("his name is Rock")

with open("text.txt") as file: # with open closes file automatically other wise we have to file.close()
    print(file.read())


## copy the file
import shutil
shutil.copyfile("source_path", "destination_path")

# moving the file
os.replace("sourch_path","destination_path")

# Delete a file
os.remove("file_path")
os.rmdir('file_path') # remove the empty directory 
shutil.rmtree("path") # dangerous. delete the whole folder or directory 

