a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]
data_list.append(15) # If you appened the list after it is created, you must address the
# variable that is created from the list. Lists are mutable but tuples are immutable.

p, q, r, s = data_list
print(p)
print(q)
print(r)
print(s)