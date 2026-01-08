import requests

s = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15',} #'Referer': 'https://forli.commercialisti.it/'}
class AspScraper:
    def __init__(self,url):
        self.url = url
    
    def _get_attr(self, s: str, attr: str) -> str:
        for q in ('"', "'"):
            token = f'{attr}={q}'
            if token in s:
                return s.split(token, 1)[1].split(q, 1)[0]
        return ''

    def extract_aspnet_hidden_inputs(self, html: str) -> dict:
        ##IN SOME CASE IT EXIST A CLASS CALLED ASPNETHIDDEN WHERE WE CAN REACH EVERY TAG OF ASP NET, IF THIS CLASS DOESN'T EXIST WE
        ##SEARCH FOR EVERY CLASS STARTING IN __ SO WE CAN'T GET THE MOST IMPORTAN VIEWSTATE EVENTVALIDATION ECC
        hidden = {}
        marker = 'class="aspNetHidden"'

        def is_hidden_input(chunk: str) -> bool:
            t = (self._get_attr(chunk, "type") or "").strip().lower()
            return t == "hidden"

        ##TRY TO READ INTO ASP NET HIDDEN DIV CLASS
        if marker in html:
            for part in html.split(marker)[1:]:
                if ">" not in part:
                    continue
                div_body = part.split(">", 1)[1].split("</div>", 1)[0]

                for chunk in div_body.split("<input")[1:]:
                    if not is_hidden_input(chunk):
                        continue

                    name = self._get_attr(chunk, "name")
                    if not name:
                        continue
                    value = self._get_attr(chunk, "value")
                    hidden[name] = value

        #IF THE CLASS ISN'T FOUND WE SEARCH IN THE ENTIRE HTML
        if marker not in html or not hidden:
            for chunk in html.split("<input")[1:]:
                if not is_hidden_input(chunk):
                    continue

                name = self._get_attr(chunk, "name")
                if not name or not name.startswith("__"):
                    continue

                value = self._get_attr(chunk, "value")
                hidden[name] = value

        return hidden


    def get_ct_tags(self, html: str, prefix: str = "ctl00$") -> list:
        ##WE TAKE EVERY HTML TAG STARTING WITH CT WE MIGHT BE WANT TO TAKE THE VALUE IF IT IS ALREADY DECLARED + SORTING NOT WORKING CORRECTLY
        tags = set()

        for attr in ("name", "id"):
            for part in html.split(f'{attr}="')[1:]:
                v = part.split('"', 1)[0]
                if v.startswith(prefix):
                    tags.add(v)

            for part in html.split(f"{attr}='")[1:]:
                v = part.split("'", 1)[0]
                if v.startswith(prefix):
                    tags.add(v)

        return sorted(tags)

    def GetAspTag(self, headers):
        session = requests.Session()
        r = session.get(self.url, headers=headers)

        hidden_inputs = self.extract_aspnet_hidden_inputs(r.text)

        ct_tags = self.get_ct_tags(r.text, prefix="ctl00$")

        return hidden_inputs, ct_tags
    
    def PostSession(self, headers, data,injectdata):
        session = requests.Session()
        data |= injectdata
        #print(data)
        r = session.post(self.url, headers=headers, data=data)
        #print(r.status_code)
        #print(session.cookies.get_dict())
        return r.text





if __name__ == '__main__':
    url1 = r'https://services.flhsmv.gov/mvcheckpersonalplate/'
    url2 = r'https://www.fpcu.it/Ricerca/RicercaIscritti.aspx?idop=51'
    url3 = r'https://forli.commercialisti.it/albo/'
    url4 = r'https://www.odcec.rimini.it/albo-iscritti/'
    url5 = r'https://anagrafe.cng.it/anagrafe/geometri.aspx'
    url6 = r'https://www.collegio.geometri.cn.it/RicercaIscritti.aspx'
    scraper = AspScraper(url6)
    tag,ct_tag = scraper.GetAspTag(s)
    #print(tag,ct_tag)
    otherData = {
        'ctl00$ContentPlaceHolder1$NIscr': '2275',
    }
    t = scraper.PostSession(headers=s , data = tag, injectdata = otherData)
    #print(t)