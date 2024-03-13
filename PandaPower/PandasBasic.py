import os


#print(os.getcwd())

current_working_directory=os.getcwd()
print('current_working_directory - ', current_working_directory)
folder_name=os.path.basename(current_working_directory)
print('flder_name - ', folder_name)