menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"], # ALT + Shift + Up/Down will move the line up or down
]

for meal in menu:
        if "spam" not in meal:
                print(meal)
                for item in meal:
                        print(item) # prints each item within list and is also named item
        else:
                print("{0} has a total count of {1} of spam"
                      .format(meal, meal.count("spam")))