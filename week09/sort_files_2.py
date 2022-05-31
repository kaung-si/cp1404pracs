import os


def main():
    """Program to store files where the user wants to."""
    file_type_to_category = {}
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_type = filename.split('.')[-1]
        if file_type not in file_type_to_category:
            file_type_key = input("What category would you like to sort {} files into?".format(file_type))
            file_type_to_category[file_type] = file_type_key
            try:
                os.mkdir(file_type_key)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(file_type_to_category[file_type], filename))


main()
