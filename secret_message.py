import os, re

def secret_message(prank_path):

        directory_list = os.listdir(prank_path) # Returns a list type

    # Loop through all the files
#     for filename in directory_list:
#         new_filename = re.sub('[0-9]', '', filename) # Returns a str type
#         os.rename( prank_path + filename, prank_path  + new_filename)
        counter = 0
        while counter < len(directory_list):
                filename = directory_list[counter]
                new_filename = re.sub('[0-9]', '', filename)
                os.rename(prank_path + filename, prank_path + new_filename)
                counter += 1



    
# New line to check after second commit



# Test Zone

p = "/Users/buyer/Desktop/prank/"

secret_message(p)

