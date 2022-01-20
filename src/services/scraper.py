from datetime import date
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self):
        self.today = date.today()
        self.url = "https://disclosures-clerk.house.gov/PublicDisclosure/FinancialDisclosure/ViewMemberSearchResult"
        self.requester = requests
        self.webpage = self.do_request_to_search()
        self.page_scraper = BeautifulSoup(self.webpage.content, "html.parser")

    def do_request_to_search(self):
        payload = {'LastName': '',
                    'FilingYear': '2022',
                    'State': '',
                    'District': ''}
        resp =  self.requester.post(self.url, data=payload)
        print(resp.text)
        return resp

