# result = True
# another_result = result
# # print(id(result)) # Bools are immutable meaning that they cannot change.
# print(id(another_result))
#
# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += 'ish'
print(id(result))
print(id(another_result)) # The another_result is immutable and the id is correct.