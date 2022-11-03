### Constants ###
SEPERATOR_LENGTH = 60

### Helper Functions ###
def seperator(line_length = SEPERATOR_LENGTH, title = ""):
    if title == "":
        for i in range(line_length):
            print('-', end="")
        print()

    else:
        line_length_reduced = line_length - len(title) # get length of line with space for title
        line_length_half = int(line_length_reduced / 2) - 1 # split length to use on both sides of title

        for i in range(line_length_half):
            print('-', end="")
        print(" " + title + " ", end="")
        for i in range(line_length_half):
            print('-', end="")
        print()