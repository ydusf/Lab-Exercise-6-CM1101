# words = ["Help", "me", "please", "they"]
# skip_words = ["please", "me", "they"]
# new_words = []

# def filter_words(words, skip_words):
#     for word in words:
#         if word not in skip_words:
#             new_words.append(word)
#     return new_words
# print(filter_words(words, skip_words))

item_id = {
    "id": "id",

    "name": "id card",

    "description":
    """You new shiny student ID card. Expires 1 June 2017.
You wonder why they have printed a suicide hotline number on it?..."""
}

item_laptop = {
    "id": "laptop",

    "name": "laptop",

    "description":
    "It has seen better days. At least it has a WiFi card!"
}

item_money = {
    "id": "money",

    "name": "money",

    "description":
    "This wad of cash is barely enough to pay your tuition fees."
}

item_biscuits = {
    "id": "biscuits",

    "name": "a pack of biscuits",

    "description": "A pack of biscuits."
}

item_pen = {
    "id": "pen",
    
    "name": "a pen",

    "description": "A basic ballpoint pen."
}

item_handbook = {
    "id": "handbook",
    
    "name": "a student handbook",

    "description": "This student handbook explains everything. Seriously."
}

room_reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},

    "items": [item_biscuits, item_handbook]
}

current_room = room_reception
inventory = [item_id, item_laptop, item_money]
items = inventory


# def list_of_items(items):
#     item_names = ""
#     counter = 0

#     for item in items:
#         counter += 1
#         if counter != len(items):
#             item_names += item["name"]+", "
#         else:
#             item_names += item["name"]
#     return item_names

# def print_room_items(room):
#     if room["items"] != []:
#         print("There is "+list_of_items(room["items"])+" here.")
#         print()

# print()
# print(room["name"].upper())
# print()
# # Display room description
# print(room["description"])
# print()
# print_room_items(room)
# print()
# def execute_take(item_id):
#     for item in current_room["items"]:
#         if item["id"] == item_id:
#             current_room["items"].remove(item)
#             inventory.append(item)
#         else:
#             print("You cannot take that.")
# execute_take("biscuits")
# print(inventory[3])

def execute_drop(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
        else:
            print("You cannot drop that.")
execute_drop("laptop")
print(inventory[0])


# if room["items"] != []:
#     print("There is "+list_of_items(room["items"])+" here.")

# print("You have "+list_of_items(items)+".")

# # print("There is "+list_of_items(items)+" here")

# print("You have "+list_of_items(inventory)+".")
# item_pen = {}
# item_back = {}

# room_reception = {"name": "Reception", "items": ["Hello"]}

# rooms = {"Reception": room_reception} 

# current_room = rooms["Reception"]


# inventory = [item_pen, item_back]

# item_id = item_pen

# if item_id in inventory:
#     print(inventory)
#     inventory.remove(item_id)
#     print(inventory)
#     current_room["items"].append(item_id)
# else:
#     print("You cannot drop that.")
# print(current_room["items"])