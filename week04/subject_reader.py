"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
class_infos = []


def main():
    """Start Program"""
    get_data()
    control = 0
    for x in range(len(class_infos)):
        print("{} is taught by {} and has {} students".format(class_infos[control][0], class_infos[control][1],
                                                              class_infos[control][2]))
        control += 1


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME, 'r')
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        class_infos.append(parts)


main()
