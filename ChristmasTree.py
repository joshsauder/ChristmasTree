import math
import threading
import os
import time
import random

def build_tree(size):
    tree, level = build_star(size)
    # New level
    level += 1
    while level <= size:
        # Add Spaces
        tree += print_spaces(size, level)
        
        # Add Body
        tree += build_body(level)

        # Add New Line
        tree += "\n"
        # New level
        level += 1

    return tree
    

def build_body(level):
    line = ""
    i = 0
    body_max = level * 2 - 1

    while (body_max > i):
        # Rotate use of x and *
        if (i%2 == 0):
            line += "x"
        else:
            line += "*"
        i += 1
    return line


def get_star_height(size):
    return math.floor(size / 4)


def build_star(size):
    tree = ""
    star_size = get_star_height(size)
    level = 1
    while (level <= star_size):
        # Add Spaces
        tree += print_spaces(size, level)
        i = level * 2 - 1
        # Add Body
        while (i > 0):
            tree += "*"
            i -= 1
        level += 1
        tree += "\n"
    # Return star_size so build_tree knows where to start body
    return tree, star_size


def print_spaces(size, level):
    line = ""
    spaces = size - level
    i = 0
    while (i < spaces):
        line += " "
        i += 1
    return line


def add_lights(tree, size):
    star_size = get_star_height(size)
    level = 0
    light_up_tree = list(tree)
    for (i, c) in enumerate(light_up_tree):
        if (c == '*' and level < star_size):
            light_up_tree[i] = '●'
        elif (c == '*' and random.uniform(0, 1) < 0.20):
            light_up_tree[i] = '●'
        elif (c == '\n'):
            level += 1
    return ''.join(light_up_tree)


def light_up_tree(tree, size):
    while True:
        # Print lit up tree
        os.system('cls' if os.name == 'nt' else 'clear')
        lit_up_tree = add_lights(tree, size)
        print(lit_up_tree)

        time.sleep(1)
        
        # Print tree turned off
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))

        time.sleep(1)


def main(size):
    tree = build_tree(size)
    light_up_tree(tree, size)

main(20)