data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_value = 100
max_value = 200

# for index in range(len(data) - 1, - 1, - 1): # range(start, stop, step)
#     if data[index] < min_value or data[index] > max_value:
#         print(index, data)
#         del data[index]
#         # print (data)
# print(index, data)

top_index = len(data) - 1
for index, x in enumerate(reversed(data)):
    if x > max_value or x < min_value:
        print(top_index - index, x)
        del data[top_index - index]

print(data)
print(len(data))