# ---- Url Shortener ---------------------------------------

# In this project,
# I make a URL shortener with three lines of Python code
# that shortens all the links and delivers them to you.

# ----------------------------------------------------------

# pip install pyshorteners
# And / Or
# python3 -m pip install pyshorteners
import pyshorteners
# Get the address of the link
input = input("Enter a link: ")
# Show the Short Version of the link
print("Shortened link: " + pyshorteners.Shortener().tinyurl.short(input))
