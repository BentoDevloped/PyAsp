from main import AspScraper

if __name__ == '__main__':
    s = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15',
    'Referer': 'https://inspectorsearch.api.org/Default.aspx',
    'Origin': 'https://inspectorsearch.api.org'}
    #'Referer': 'https://forli.commercialisti.it/'}

    url1 = r'https://services.flhsmv.gov/mvcheckpersonalplate/'
    url2 = r'https://www.fpcu.it/Ricerca/RicercaIscritti.aspx?idop=51'
    url3 = r'https://forli.commercialisti.it/albo/'
    url4 = r'https://www.odcec.rimini.it/albo-iscritti/'
    url5 = r'https://anagrafe.cng.it/anagrafe/geometri.aspx'
    url6 = r'https://www.collegio.geometri.cn.it/RicercaIscritti.aspx'
    url7 = r'https://my.libf.ac.uk/ProfessionalServicesRegister.aspx'
    url8 = r'https://inspectorsearch.api.org/default.aspx'
    scraper = AspScraper(url8)
    tag,ct_tag = scraper.GetAspTag(s)
    #print("tag",ct_tag)
    otherData = {
        'ctl00$MainContent$CheckBoxList1$22': 'on',
        'ctl00$MainContent$SearchName': 'smith',

        }
    t = scraper.PostSession(headers=s , data = tag, injectdata = otherData)
    print(t)
