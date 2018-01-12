plist = {'Sandwitch' : 4, 'apple' : 12, 'cups' : 4, 'cookies' : 8000}
def picnicList(pdict, i, j):
    print('Picnic List'.center(i + j,'*'))
    for a,b in pdict.items():
        print(a.ljust(i, '-') + str(b).rjust(j))
    print()

picnicList(plist, 12, 5)
picnicList(plist, 20, 6)
