def strg(span):
    for i in span[ : -1]:
        print(i + ' ',end = '')
    print('and '+span[-1])


span = ['cat', 'bat', 'rat', 'elephant']
strg(span)
