import sys

def build_tree(size):
    i = build_star(size) + 1
    while i <= size:
        # Add Spaces
        line = print_spaces(size, i)
        
        # Add Content
        j = 0
        content_max = i * 2 - 1
        
        while (content_max > j):
            if (j%2 == 0):
                line += "x"
            else:
                line += "*"
            j += 1
        
        print(line)
        i += 1

def build_star(size):
    star_size = size / 3
    i = 1
    while (i <= star_size):
        line = print_spaces(size, i)
        j = i * 2 - 1
        while (j > 0):
            line += "*"
            j -= 1
        i += 1
        print(line)
    return star_size

def print_spaces(size, level):
    line = ""
    spaces = size - level
    space_temp = 0
    while (space_temp < spaces):
        line += " "
        space_temp += 1
    return line
    

def main(size):
    build_tree(size)

main(10)