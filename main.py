username= "admin"
password_length= 12
if username == "admin":
    if password_length >= 10:
        print("Login succesful")
    else:
        password_length < 10
        print("Admin password incorrect")
else:
    username == "guest"
    if password_length >= 6:
        print("Login succesful")
    else:
        password_length < 6
        print("User password must be 6+")