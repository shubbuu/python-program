import re, pyperclip, sys
text = pyperclip.paste()
num = re.compile(r'\+.*')
email = re.compile(r'.*@.*')
mo1 = num.findall(text)
mo2 = email.findall(text)
if len(mo1) > 0 :
    print('\n'.join(mo1))
else :
    print('No number found.')
    
if len(mo2) > 0 :
    print('\n'.join(mo2))
else :
    print('No email found.')
