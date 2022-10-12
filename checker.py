# words = ["Help", "me", "please", "they"]
# skip_words = ["please", "me", "they"]
# new_words = []

# def filter_words(words, skip_words):
#     for word in words:
#         if word not in skip_words:
#             new_words.append(word)
#     return new_words
# print(filter_words(words, skip_words))

items = ["Shoe", "Backpack", "Pebble", "Tra"]
inventory = ["Orange", "a banana", "a player"]

def list_of_items(items):
    item_names = ""
    items = ["a shoe", "a backpack", "Pebble", "Tra"]
    counter = 0

    for item in items:
        counter += 1
        if counter != len(items):
            item_names += item+", "
        else:
            item_names += item
    return item_names

# print("There is "+list_of_items(items)+" here")

print("You have "+list_of_items(inventory)+".")