import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


nr_letter = int(input("Enter the number of letter would you like in your password:"))
nr_symbol = int(input("Enter the number of symbol would you like in your password:"))
nr_number = int(input("Enter the number of number would you like in your password:"))

# Easy Level
# password = ""
# for char in range(1, nr_letter):
#   password += random.choice(letters)
#
# for nnum in range(1, nr_number):
#   password += random.choice(numbers)
#
# for sym in range(1, nr_symbol):
#   password += random.choice(symbols)
#
# print(password)



#Hard Level

password_list = []

for char in range(1, nr_letter + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbol + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_number + 1):
  password_list.append(random.choice(numbers))


# It will print the list of elements which will present in
# print(password_list)
# random.shuffle(password_list)
# print(password_list)

pswd = ""
for char in password_list:
  pswd += char
print(pswd)

