import pprint
message = '''Most of the code examples in the book are shown with input and output as it would
appear executed in the IPython shell.'''
count = {}
for i in message:
    count.setdefault(i, 0)
    count[i] += 1

pprint.pprint(count)
