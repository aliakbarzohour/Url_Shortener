import pyshorteners

input = input("Enter a link: ")
print("Shortened link: " + pyshorteners.Shortener().tinyurl.short(input))