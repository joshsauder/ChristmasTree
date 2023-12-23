import sys
import math

def build_tree(size):
    level = build_star(size) + 1
    while level <= size:
        # Add Spaces
        line = print_spaces(size, level)
        
        # Add Body
        line = build_body(level, line)
        
        print(line)
        level += 1

def build_body(level, line):
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

def build_star(size):
    star_size = math.floor(size / 4)
    level = 1
    while (level <= star_size):
        # Add Spaces
        line = print_spaces(size, level)
        i = level * 2 - 1
        # Add Body
        while (i > 0):
            line += "*"
            i -= 1
        level += 1
        print(line)
    # Return star_size so build_tree knows where to start body
    return star_size

def print_spaces(size, level):
    line = ""
    spaces = size - level
    i = 0
    while (i < spaces):
        line += " "
        i += 1
    return line
    

def main(size):
    build_tree(size)

main(12)