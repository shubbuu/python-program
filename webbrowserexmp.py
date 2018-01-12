import pyperclip
import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('www.'+address+'.com')
