# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities = []
#
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:

"""
using append  and strip here

"""
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda MAy", "2011", (
#     (1, "Pulling the Rug"), (2,"Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

"""
    Evaluate the given source in the context of globals and locals.
    
    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
    
"""

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
