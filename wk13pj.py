
import os

cwd = os.getcwd()

files = os.listdir(cwd)

dict_list = []

for file_name in files:
    file_path = os.path.join(cwd, file_name)
    file_size = os.path.getsize(file_path)
    
    file_info = {
        'file_name': file_name,
        'file_path': file_path,
        'file_size': file_size,
    }
    
    dict_list.append(file_info)

for file_info in dict_list:
    print(file_info)
    
