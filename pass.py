import pyperclip
password = {'gmail' : '123', 'facebook' : '456'}
print('Enter account name : ')
n = input()
if n in password.keys():
    pyperclip.copy(password[n])
    print('password is copied to clipboard')

else :
    print('u have entered wrong key.')
