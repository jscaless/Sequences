for index, character in enumerate('abcdefgh'):
    # Without enumerate, index would not work;
    # i/Index gives us a number placement and character gives the parts
    print(index, character)

for s in enumerate('abcedfgh'):
    # If we only use one variable with enumerate, it gives us a tuple with the following index.
    index, character = s
    print(index, character)

index, character = ('0','a')
print(index)
print(character)