from datetime import date
import requests
from bs4 import BeautifulSoup
import pdfbox



class Scraper:

    def __init__(self, year):
        self.today = date.today()
        self.url = "https://disclosures-clerk.house.gov/PublicDisclosure/FinancialDisclosure/ViewMemberSearchResult"
        self.requester = requests
        self.year = year
        self.webpage = self.do_request_to_search(year)
        self.page_scraper = BeautifulSoup(self.webpage.content, "html.parser")

    def do_request_to_search(self, year):
        payload = {'LastName': '',
                    'FilingYear': str(year),
                    'State': '',
                    'District': ''}
        resp = self.requester.post(self.url, data=payload)
        return resp

    def download_pdfs(self):
        links = self.page_scraper.find_all('a')
        print(len(links))
        done = False
        for link in links:
            if '.pdf' in link.get('href', []):
                response = requests.get("https://disclosures-clerk.house.gov" + link.get('href'))
                name = str(link.text.split("..")[1].replace(" ", "")) + str(self.year) + ".pdf"
                pdf = open("/home/peeter/PycharmProjects/fastApiProject/src/resources/records/" + name,  'wb+')
                pdf.write(response.content)
                pdf.close()

                print("File ", link.get('href'), " downloaded")

                # Convert pdf to txt file
                pdfbox.PDFBox().extract_text("/home/peeter/PycharmProjects/fastApiProject/src/resources/records/" + name)


