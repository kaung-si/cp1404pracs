import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_type = filename.split('.')[-1]
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass
        os.rename(filename, f"{file_type}/{filename}")


main()