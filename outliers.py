# data = [4, 5, 101, 150, 165, 178, 180, 185, 189, 192, 195, 198, 200,
        # 210, 230, 400, 450]
# data = [101, 150, 165, 178, 180, 185, 189, 192, 195, 198, 200,
       # 210, 230, 400, 450]
#data = [4, 5, 101, 150, 165, 178, 180, 185, 189, 192, 195, 198, 200,
     #   210, 230]
data = [101, 150, 165, 178, 180, 185, 189, 192, 195, 198, 200,
        210, 230]

# Run edge cases, research Wikipedia
# Run the high end numbers and low.

min_value = 100
max_value = 250

# iterable - a python object capable of returning its member one at a time
# iterable example is a list. x = [1, 2, 3, 4]
# iterator processes each number at a time within the list/iterable
# enumerate - adds a counter to a iterable for a task.

# Removes lower numerical values
stop = 0
for index, value in enumerate(data):
        if value >= min_value:
                stop = index
                break
print(stop) # for debugging
del data[:stop]
print(data)

# Removing higher numerical values
# Remember list values are now different due to deleting data
stop_inverse = 0
for index in range(len(data) -1, -1, -1): # range(start, stop, step)
        if data[index] <= max_value:
                stop_inverse = index
                break
print(stop_inverse) # for debugging
del data[stop_inverse:]
print(data)
