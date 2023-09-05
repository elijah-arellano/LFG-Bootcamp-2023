#check if a file exists
#we will use a package called os Module

import os

file_exists = os.path.isfile('data.csv')
print(file_exists)

#open a file

csv_file = open("data.csv", mode='+a', newline='')