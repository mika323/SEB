import string

password = input('Enter password: ')
isValid = True
allowed_sym = string.ascii_lowercase + string.ascii_uppercase + string.digits + '*-#'
special_sym = '*-#'
errors = ''

if len(password) != 8:
    errors = errors + 'The password length is not equal to 8.\n'
    isValid = False
if password.lower() == password:
    errors = errors + 'There are no capital letters in the password.\n'
    isValid = False
if password.upper() == password:
    errors = errors + 'There are no lowercase letters in the password.\n'
    isValid = False
if not any(char.isdigit() for char in password):
    errors = errors + 'There are no digits in the password.\n'
if not any(char in special_sym for char in password):
    errors = errors + 'There are no special symbols in the password.\n'
if any(char not in allowed_sym for char in password):
    errors = errors + 'Unauthorized characters are used in the password.\n'
if isValid:
    print('The password is valid.')
else:
    print('The password is not valid:')
    print(errors)



