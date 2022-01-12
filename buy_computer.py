available_parts = ['Computer',
                   'Monitor',
                   'Keyboard',
                   'Mouse',
                   # 'Mouse Mat',
                   'HDMI Cable',
                   'Flash Storage',
                   'To Finish']
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = [] # creates empty list for i range
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
current_choice = '-'
computer_parts = [] # creates empty list for while and if statement

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index] # Index gives the number within the list
        if chosen_part in computer_parts: # If chosen_part number is already
                                        # in computer_parts. Typing it again will remove it
            print('Removing {}'.format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print('Adding {}'.format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print('Please add the options for the list below:')
        for number, parts in enumerate(available_parts):
            print('{0}: {1}'.format(number + 1, parts))
    current_choice = input()
print('Printing Computer Parts List...please wait')
print(computer_parts)