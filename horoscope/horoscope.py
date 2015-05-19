import urllib2
from bs4 import BeautifulSoup

def horoscope(sign):
    url = 'http://www.astrology.com/horoscope/daily/%s.html'%sign
    html_doc = urllib2.urlopen(url)
    soup = BeautifulSoup(html_doc.read())
    date = soup.find_all('span',{'class','page-horoscope-date-font'})[0].get_text()
    text = soup.find_all('div',{'class','page-horoscope-text'})[0].get_text()
    print "%s - %s\n\n%s" % (sign.capitalize(), date, text)

if __name__ == '__main__':
    try:
        sunsign = raw_input ("Enter Your Sunsign : ")
        horoscope(sunsign)
    except IndexError:
        print "Please enter a valid zodiac sign.\nUsage example: taurus"
