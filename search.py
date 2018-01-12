import sys, requests, bs4, webbrowser
searchItem = sys.argv[1]
res = requests.get('https://www.google.co.in/search?q=' + searchItem)
soup = bs4.BeautifulSoup(res.text)
sel = soup.select('.r a')
x = min(3,len(sel))
for i in range(x):
    webbrowser.open('http://google.co.in' + sel[i].get('href'))
