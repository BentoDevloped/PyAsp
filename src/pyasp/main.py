import requests

s = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15'}

class AspScraper:
    def __init__(self,url):
        self.url = url
    
    def get_hidden_value(self,html, name):
        try:
            return html.split(f'"{name}" value="')[1].split('"')[0]
        except IndexError:
            return ''
    
    def GetAspHiddenTag(self, headers):
        session = requests.Session()
        
        r = session.get(self.url, headers=headers)
        __VIEWSTATE = self.get_hidden_value(r.text, '__VIEWSTATE')
        __EVENTVALIDATION = self.get_hidden_value(r.text, '__EVENTVALIDATION')
        __EVENTARGUMENT = self.get_hidden_value(r.text, '__EVENTARGUMENT')
        __VIEWSTATEGENERATOR = self.get_hidden_value(r.text, '__VIEWSTATEGENERATOR')
        print(__EVENTVALIDATION)








if __name__ == '__main__':
    scraper = AspScraper('https://services.flhsmv.gov/mvcheckpersonalplate/')
    scraper.GetAspHiddenTag(s)
        