
import time
import os
import webbrowser
import re
from pathlib import Path

URL = 'https://automatetheboringstuff.com/2e/chapter'
MENU = '''
Choose chapter from the list:
1 - Python Basics
2 - Flow Control
3 - Functions
4 - Lists
5 - Dictionaries and Structuring Data
6 - Manipulating Strings
7 - Pattern Matching with Regular Expressions
8 - Input Validation
9 - Reading and Writing Files
10 - Organizing Files
11 - Debugging
12 - Web Scraping
13 - Working with Excel Spreadsheets
14 - Working with Google Spreadsheets
15 - Working with PDF and Word Documents
16 - Working with CSV Files and JSON Data
17 - Keeping Time, Scheduling Tasks, and Launching Programs
18 - Sending Email and Text Messages
19 - Manipulating Images
20 - Controlling the Keyboard and Mouse with GUI Automation

Type chapter number here:
'''
PATH = Path.home() / Path('Python', 'automate_boring_stuff')

def is_valid(input: str) -> bool:
    ''' Return True when input is a valid chapter number, False otherwise.'''

    regex = re.compile(r'^\s*[1-9][0-9]{,1}\s*$')
    mo = regex.search(input)
    if mo == None:
        return False
    if int(input) > 20: 
        return False
    return True
    
chapter = input(MENU)
if is_valid(chapter):
    chapter = chapter.strip()
    webbrowser.open(URL + chapter)
    os.chdir(PATH)
    os.system('gnome-terminal')
else:
    print('Chapter format is invalid or given number is too big.\nClosing terminal in 2 seconds.')
    time.sleep(1.5)

# os.chdir(PATH)
