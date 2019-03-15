import bs4 as bs
import urllib.request

# Frustration level is high, I would like the code to complete this so I can replicate on the 
# rest of the web page,  and https://finance.yahoo.com/quote/NFLX?p=NFLX
# many thanks!!!

# I want the code to utilize beautiful soup


# I would like to read "sample ticker read in file.csv" and loop through extracting data

sauce=urllib.request.urlopen('https://finance.yahoo.com/quote/NFLX/analysis?p=NFLX').read()
soup=bs.BeautifulSoup(sauce,'lxml')
#print(soup)



badges = soup.body.find('div', attrs={'class': 'Pos(r) Fl(start) Fz(xs) C($c-fuji-grey-j) '})
print(badges)
#for span in badges.span.find_all('span', recursive=False):
#    print(span.text)


#Export data into "Export Sample 1.csv" and "Export Sample 2.csv"
csv" and "Export Sample 2.csv"