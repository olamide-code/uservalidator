#validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username \n")

if len(username) > 12:
    print("your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("your username can't contain spaces")
elif not username.isalpha():
    print("your name")
else: 
    print(f"welcome {username}")