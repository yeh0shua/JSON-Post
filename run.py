#! /usr/bin/env python3

import os, sys
import requests
import json

# Takes an input path and saves it as dir
dir = sys.argv[1]

# Generates a list of files within dir
files_in_dir = os.listdir(dir)

data_dict = {}

# Iterates over each file in dir
for file in files_in_dir:
    # Opens the file
    with open(dir + '/' + file) as text_file:
        # Read the contents of file into a list and splits the list by each new line.
        line_list = text_file.read()
        line_list = line_list.split('\n')

        # Writes the contents of the split line list into a dictionary.
        data_dict['title'] = line_list[0]
        data_dict['name'] = line_list[1]
        data_dict['date'] = line_list[2]
        data_dict['feedback'] = line_list[3]

        json_dict = json.dumps(data_dict, indent = 4)

        response = requests.post('http://localhost/feedback/', data=data_dict)
        print(response)




