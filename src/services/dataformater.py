import sys
import os
sys.path.append(os.path.abspath("/home/peeter/PycharmProjects/fastApiProject/src/services"))
import scraper
path_to_records = "/home/peeter/PycharmProjects/fastApiProject/src/resources/records/"

class Formatter:
    """
    Class formats txts that have been converted from pdfs to csvs with useful information
    """

    def __init__(self, year):

        #if os.path.exists(path_to_records + f"csvs/{str(year)}") is False:
         #   os.mkdir(path_to_records + f"csvs/{str(year)}")
        self.year = year
        #if os.path.exists(path_to_records + f"txts/{str(year)}") is False:
        #    scraper.Scraper(year)
        self.file_names = os.listdir(path_to_records + f"txts/{str(year)}")
        self.year = year

    def create_csvs_from_text(self):
        for i in self.file_names:
            print(f"Formatting {i}")
            txt = open(path_to_records + f"txts/{str(self.year)}/" + i, 'r')
            try:
                text = txt.read().upper()
                text = text.split("TRANSACTIONS")
                # transaction splits the file into two where the second part consists of financial information
                text = text[1].split('gfedc'.upper())[:-2]
                # gfedc means ---- in pdf reading terms so where splitting the text even further and cutting out
                # the last part because it is the certificate
                owns = text
                for j in owns:
                    j = j.split('\n') # split at newline so it would look nicer
                    for m in j:
                        print(m)
            except IndexError:
                print(f"Trouble reading {i}")
