def check_pass(password):

    symbols = ['*', '-', '#']
    validPassword = True

    if len(password) != 8:
        print('Password has less than 8 characters or more')
        validPassword = False
    if not any(char in symbols for char in password):
        print('Password has no any symbols like *-#')
        validPassword = False
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        validPassword = False
    if not any(char.isupper() for char in password):
        print('Password has no any uppercase letter')
        validPassword = False
    if not any(char.islower() for char in password):
        print('Password has no any lowercase letter')
        validPassword = False

    if validPassword:
        print('Password is valid')


password = input("Please enter your password:\n")
check_pass(password)
