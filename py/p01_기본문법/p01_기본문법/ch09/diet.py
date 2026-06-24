

def print_valid_menu():  
    for key, value in menu.items():
        if value > 500:
            print("{}:X".format(key))
        else:
            print("{}:O".format(key))