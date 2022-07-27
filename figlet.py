from pyfiglet import Figlet
import shutil
import sys

a=sys.argv[0]
print(a)

columns = shutil.get_terminal_size().columns
#print("hello world".center(columns))
f = Figlet(font='slant')
a=input("Enter:")
a=' '*(columns//9)+a
figlet_str=f.renderText(a)
print(columns)

#print(a*(columns//2),end='')
#print("lets see")
print(figlet_str.center(columns))