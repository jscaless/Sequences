# t =  ("a", "b", "c")
# print(t) # Prints a Tuple not a List, Lists are in square brackets
# Tuples are in parantheses, always use parantheses around tuples
# Tuples can be within Tuples as well. Below shows tuples within a list.
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for title, artist, year in albums:
    print("Album: {0} | Artist: {1} | Year: {2}"
          .format(title, artist, year))

for album in albums:
    title, artist, year = album
    print("Album: {0} | Artist: {1} | Year: {2}"
          .format(title, artist, year))
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)
# title, artist, year = metallica
# print(metallica)
#
# table = ("Coffee Table", 100, 100, 250)
# product_name, length, width, height = table
# print(table[1] * table [2])
