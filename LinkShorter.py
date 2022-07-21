# ---- Url Shortener ---------------------------------------

# In this project, 
# I make a URL shortener with three lines of Python code 
# that shortens all the links and delivers them to you.

# ----------------------------------------------------------

# pip install pyshorteners 
# And / Or  
# python3 -m pip install pyshorteners
import pyshorteners

input = input("Enter a link: ")
print("Shortened link: " + pyshorteners.Shortener().tinyurl.short(input))