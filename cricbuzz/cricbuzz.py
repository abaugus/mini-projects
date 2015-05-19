import urllib2
from bs4 import BeautifulSoup

def cricbuzz():
        url="http://www.cricbuzz.com/cricket-series/2330/indian-premier-league-2015"
        print "Getting updates from Cricbuzz  . . . . . . . . ."
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())
        headlines=soup.find_all('h3',{ 'class' : 'cb-headline'})
        for headline in headlines:
                print(headline.string)
if __name__ == "__main__":
        cricbuzz()
