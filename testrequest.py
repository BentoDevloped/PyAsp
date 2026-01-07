import requests

session = requests.Session()


#THE ONLY HEADER REQUIRED IS THE REFERER
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Referer': 'https://forli.commercialisti.it/'
           }
url = r'https://www.fpcu.it/Ricerca/RicercaIscritti.aspx?idop=51'

r = session.get(url, headers=headers)

#print(r.text)


#UNDERSCORED ARE THE TAG OF ASPX ONLY VIEWSTATE AND EVENTTARGET ARE NECESSARY TO MAKE THE REQUEST WORK

__VIEWSTATE = r.text.split('__VIEWSTATE" value="')[1].split('"')[0]
__EVENTVALIDATION = r.text.split('__EVENTVALIDATION" value="')[1].split('"')[0]
__EVENTTARGET = 'ctl00$ContentPlaceHolder1$RicercaAlbo1$CtlButtonSearch'
__EVENTARGUMENT = r.text.split('__EVENTARGUMENT" value="')[1].split('"')[0]
__VIEWSTATEGENERATOR = r.text.split('__VIEWSTATEGENERATOR" value="')[1].split('"')[0]
__ASYNCPOST = 'true'
#THE DATA PAYLOAD NEED TO CONTAIN VIEWSTATE EVENTTARGET AND THE CLIENTSTATE 
data = {
    '__VIEWSTATE': __VIEWSTATE,
    #'__EVENTVALIDATION': __EVENTVALIDATION,
    '__EVENTTARGET': __EVENTTARGET,
    #'ctl00$ContentPlaceHolder1$RicercaAlbo1$cbSezione': 'Sezione A',
    'ctl00_ContentPlaceHolder1_RicercaAlbo1_cbSezione_ClientState': '{"logEntries":[],"value":"50","text":"Sezione A","enabled":true,"checkedIndices":[],"checkedItemsTextOverflows":false}'
}
#print(re.text)

r = session.post(url, headers=headers, data=data)

print(r.text)