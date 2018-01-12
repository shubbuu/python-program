import pyperclip
message = pyperclip.paste()
list = message.split('\n')
for i in range(len(list)):
    list[i] = '* ' + list[i]

message = '\n'.join(list)
print(message)
