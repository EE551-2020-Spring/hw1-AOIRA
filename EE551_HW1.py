

"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"

    # Assign a string "Stevens" to a variable y
    y = "Stevens"

    # Repeat variable y 5 times
    z = y * 5

    # What is the length of z?
    length = len(z)

    # Concatenate variable y with string " is good"
    m = y + " is good"

    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = y.replace('good', 'awesome')

    return x, y, z, length, m, n
    # return x


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p = n.split(' ')
    print(p)

    # Get all the items past the first of the third substring
    r = p[1:]
    print(r)

    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    c = [1, 4, 5], [6, 10, 11], [12, 17, 38]
    # c = 1
    print(c)
    

    # Collect the items in the last column of matrix A using list comprehension
    d = [x[-1]for x in c]
    print(d)
   

    # Collect only the even items of the diagonal of matrix A using list comprehension
    o = [c[i][i] for i in range(0,3) if c[i][i] % 2 == 0]


    print(o)

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    ss = "Stevens"
    oo = [ord(ss[i]) for i in range (0,len(ss))]
    print(oo)
    # for i in range()
    # oo.append(ord())
    
    return p, r, c, d, o
    # return 1


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    a = {"fruit":"apple", "quantity":4, "color":"green"}

    # Get the item in dictionary f that the key "fruit" maps to
    f = a["fruit"]
    print(f)

    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    a["quantity"] = a["quantity"] + 1
    print(a)

    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    p = {"name":{"first_name" : "Grace", "last_name" : "Hopper"}, "jobs":["scientist", "engineer"], "age":85}
    print(p)

    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    print(p["jobs"])
    p["jobs"].append("programmer")
    print(p["jobs"])

    # Get the third job Grace has that you recently added
    k = p["jobs"][-1]
    print(k)

    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    kk = sorted("amazing_grace")
    
    print(kk)

    return a, f, p, k
    # return 1

numbers_and_strings()
lists()
dictionaries()







