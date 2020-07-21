"""
Examples of string methods
"""

# Accessing characters in a string
# Index starts from zero
first = "nyc"[0]
city = "sfo"
print(first)
ft = city[0]
print(ft)


"""
len()        # helps determine the length of a string
lower()      # converts a string to lower case
upper()      # converts a string to upper case
str()        # converts something into a string
"""

stri = "This Is a Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))


"""
Concatenation of strings
"""

print("Hello"+" "+"World!")
print(first + " " + city)
