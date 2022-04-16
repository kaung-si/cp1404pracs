def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        question = input("Is your name {} (Y/n) ".format(get_name_from_email(email)))
        if question != "" and question.upper() != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    name = email.split('@')[0]
    name_parts = name.split('.')
    full_name = " ".join(name_parts).title()
    return full_name


if __name__ == '__main__':
    main()