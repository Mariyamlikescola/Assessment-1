# Defining the correct password
correct_password = "12345"
max_attempts = 5
attempts = 0

# Using a while loop to repeatedly ask for the password until the correct one is entered or attempts are exhausted
while attempts < max_attempts:
    entered_password = input("Enter the password: ")
    
    if entered_password == correct_password:
        print("Your password is correct, Access granted!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("The given password is incorrect. Authorities have been alerted!")