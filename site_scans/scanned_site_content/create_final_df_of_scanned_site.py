import os
#
# # print("Path at terminal when executing this file")
# # print(os.getcwd() + "\n")
# #
# # print("This file path, relative to os.getcwd()")
# # print(__file__ + "\n")
# #
# # print("This file full path (following symlinks)")
# full_path = os.path.realpath(__file__)
# print(full_path + "\n")
#
# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")

# print("This file directory only")
# print(os.path.dirname(full_path))
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
   for name in files:
       complete_file_name = os.path.join(root, name)
       if ".DS_Store" in complete_file_name:
           continue
       elif "original_scanned" in complete_file_name:
           continue
       elif ".py" in complete_file_name:
           continue
       else:
           print('file: ', complete_file_name)
   # for name in dirs:
   #    print(os.path.join(root, name))