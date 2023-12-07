"""
Create a Python file named lab_8-7.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using the nested list rows from the "Nested Data" slide, write a function that prints each person's name 
BONUS: Make each name be possessive. Remember, if a name ends in s, only add an apostrophe. If the name does not end in s, add, 's.

"""
def print_possessive_names(rows):
    for row in rows:
        for name in row:
            possessive_name = name + "'" if name.endswith('s') else name + "'s"
            print(possessive_name)

#this is a Example nested list
rows = [
    ["Darick", "Eugene", "Kyle", "Azaan"],
    ["Ryan", "Phil", "Eman", "Alex", "Nicholas"],
    ["Christian", "Josh", "Matt", "Francesco"],
    ["Patrick", "Nico", "Trevayne"]
]

# this is what I will Call the function with your data
print_possessive_names(rows)
