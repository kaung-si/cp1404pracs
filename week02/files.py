# 1.
name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
print(f"Your name is {in_file.read()}")
in_file.close()

# 3. Method 1
num_file = open("numbers.txt", 'r')
total = 0
for x in range(2):
    total += int(num_file.readline())
print(total)
num_file.close()

# 3. Method 2
number_file = open("numbers.txt", 'r')
first_num = int(number_file.readline())
second_num = int(number_file.readline())
total = first_num + second_num
print("{} + {} = {}".format(first_num, second_num, total))
number_file.close()

# 4.
n_file = open("numbers.txt", 'r')
total = 0
for x in n_file:
    total += int(x)
print(total)
n_file.close()


