
file = "C:\\Users\\dylant.barnett\\Documents\\Notes\\3560_globalconfig.txt"

with open(file) as fhand:
    for line in fhand:
        print(f'"{line.rstrip()}",',end="\n")
        