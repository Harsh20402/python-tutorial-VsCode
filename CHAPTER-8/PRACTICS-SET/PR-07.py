# Write a python function to remove a given word from a list ad strip it at the same time.

# Function to remove a word from a list and strip whitespace
def word_remove(param1, param2):
    new_list = []
    for item in param1:
        item = item.strip()  # Strip whitespace
        if item != param2:   # Check after stripping
            new_list.append(item)
    return ", ".join(new_list)

# Function to collect items from user
def add_items():
    item_no = int(input("How many items do you want to add: ").strip())
    print("Please, enter the items: ")
    user_item = []
    for x in range(1, item_no + 1):
        item = input(f"Enter item {x}: ")
        user_item.append(item)
    
    print(f"The following words are: {', '.join(user_item)}.")
    del_item = input("Please, enter the word to remove: ").strip()
    return user_item, del_item

# Calling the function and displaying the result
final_item = add_items()

print(f"After removing the word '{final_item[1]}', the final words are: {word_remove(final_item[0], final_item[1])}.")




