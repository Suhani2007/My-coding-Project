# print('''
# Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.

# Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.''')
        
# import pyttsx3
# engine = pyttsx3.init() 
# engine.say("I will speak this text")
# engine.runAndWait()

import os

# path to the directory you want to list
path = "/"

try:
    # get list of all files and folders
    contents = os.listdir(path)
    
    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Error: Directory not found!")
except PermissionError:
    print("Error: Permission denied!")
