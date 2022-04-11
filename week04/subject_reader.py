"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
class_infos = []


def main():
    """Start Program"""
    get_data()
    for x in range(len(class_infos)):
        print("{} is taught by {} and has {} students".format(class_infos[x][0], class_infos[x][1],
                                                              class_infos[x][2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME, 'r')
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        class_infos.append(parts)
    input_file.close()


main()
