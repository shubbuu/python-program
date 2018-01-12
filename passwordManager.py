import sys, pyperclip
password = {'gmail' : '12345', 'facebook' : '45678'}
if len(sys.argv) > 1:
    account = sys.argv[1]
    if account in password :
        pyperclip.copy(password[account])
        print('password for ' + account + ' is : ')
        
else :
    print('arguement is less than 2')
