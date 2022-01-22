import os
import sys
sys.path.append("..")
import paths
import scraper
class Formater:
    """
    Class formats txts that have been converted from pdfs to csvs with useful information
    """

    def __init__(self, year):
        if os.path.exists(paths.path_to_records + f"csvs/{str(year)}") is False:
            os.mkdir(paths.path_to_records + f"csvs/{str(year)}")
        self.year = year
        if os.path.exists(paths.path_to_records + f"txts/{str(year)}") is False:
            scraper.Scraper(year)
        self.file_names = os.listdir(paths.path_to_records + f"txts/{str(year)}")
        self.year = year

    def create_csvs_from_text(self):
        for i in self.file_names:
            txt = open(paths.path_to_records + f"txts/{str(self.year)}/" + i, 'r')
            text = txt.read()
            print(text)
            break

