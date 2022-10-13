from game import *
from gameparser import *
from items import *
from map import *
from player import *

# def execute_take(item_id):
#     for item in current_room["items"]:
#         if item["id"] == item_id:
#             current_room["items"].remove(item)
#             inventory.append(item)

# for i in inventory:
#     print(i["id"], end=', \n')
# execute_take("biscuits")
# for i in inventory:
#     print(i["id"], end=', \n')

# def execute_drop(item_id):
#     for item in inventory:
#         if item["id"] == item_id:
#             inventory.remove(item)
#             current_room["items"].append(item)

# for i in inventory:
#     print(i["id"], end=', \n')
# execute_drop("laptop")
# for i in inventory:
#     print(i["id"], end=', \n')

def execute_go(direction):

    global current_room

    exits = current_room["exits"]

    if is_valid_exit(exits, direction):
        current_room = move(exits, direction)
        print(current_room["name"])
    else:
        print("You cannot go there.")
execute_go("south")

print(list_of_items(inventory))
print(normalise_input("How about I go through that little passage to the south..."))

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