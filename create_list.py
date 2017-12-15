 # list to hold on to out items
shopping_list = []

# print out instructions
print("What should we ick up at the store?")
print("Enter 'DONE' to stop adding items")

while True:
    new_item = raw_input("> ")

    if new_item == 'DONE':
        break
    shopping_list.append(new_item)

# be able to quit the app
print("Here is everything in the list")

# print out the list
print(shopping_list)
