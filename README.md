#JSON Post

This Python program receives text files as input and converts the data to 
JSON format to POST to a Django web server.

The program takes a directory as an input path. It then iterates through
each text file in the directory and for each line in the file, assigns key
and values.

The dictionary is converted into a JSON object, and then the program requests
the web server to accept the data.

The result of the request is printed to the screen.
