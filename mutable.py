shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list) # Lists are mutable and the id will remain the same even though something new.
print(id(shopping_list)) # Strings are immutable and Lists are mutable. If a new object is created it is immutable.
print(another_list)

a = b = c = d = e = f = another_list
# a = another_list
# b = another_list
# c = another_list
# d = another_list
# e = another_list
# f = another_list
print(a)

print("Adding cream")
b.append("cream")
c.append("deez nuts")
print(c)
print(d)