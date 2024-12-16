correct_username = "MaiHoonKapil"
correct_password = "ThalaForReason"


username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == correct_username) and (password == correct_password):
    print("Login successful!")
else:
    print("Login failed! Please check your username and password.")