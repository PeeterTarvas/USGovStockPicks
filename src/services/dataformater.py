import sys
import os
import regex as re

sys.path.append(os.path.abspath("/home/peeter/PycharmProjects/fastApiProject/src/services"))
path_to_records = "/home/peeter/PycharmProjects/fastApiProject/src/resources/records/"


class Formatter:
    """
    Class formats txts that have been converted from pdfs to csvs with useful information
    """

    def __init__(self, year):
        # these os commands will give an error because for some reason the interpreter doesn't find the correct path
        # if os.path.exists(path_to_records + f"csvs/{str(year)}") is False:
        #   os.mkdir(path_to_records + f"csvs/{str(year)}")
        self.year = year
        # if os.path.exists(path_to_records + f"txts/{str(year)}") is False:
        #    scraper.Scraper(year)
        self.file_names = os.listdir(path_to_records + f"txts/{str(year)}")
        self.year = year

    def create_csvs_from_text(self):
        databs: dict = {}
        for i in self.file_names:
            print(f"Formatting {i}")
            txt = open(path_to_records + f"txts/{str(self.year)}/" + i, 'r')
            try:
                text = txt.read().upper()
                # Find the full name of repr
                name = re.findall("(?<=NAME: HON.\s).{3,}", text)[0]
                databs[name] = []


                text = text.split("TRANSACTIONS")
                # transaction splits the file into two where the second part consists of financial information
                text = text[1].split('gfedc'.upper())[:-2]
                # gfedc means ---- in pdf reading terms so where splitting the text even further and cutting out
                # the last part because it is the certificate
                owns = text
                for field in owns:
                    asset = self.find_stock_and_amnt(field)[0].replace("\n", " ")
                    databs.get(name).append(asset)

            except IndexError:
                print(f"Trouble reading {i}")
        for k, i in databs.items():
            print(f"{k}: has {i}\n")

    def find_stock_and_amnt(self, form_filed: str):
        """
        This could be done with splitting text from the last $
        Data is usually on the last two lines but not always
        Before data there is always DESCRIPTION: ... or GAINS > 200$? or FILING ID .... or SUBHOLDING OF: ... or
        just only FILING STATUS: NEW, but this is a rare case or
        each time these indicators will end with \n where the next line will be data

        The order of the ifs is important because some strings have many variants and the current method identifies
        which one is the closest to data

        :param form_filed:
        :return:
        """

        if "$200?" in form_filed:
            # This finds everything after $200 and if it is a multi line statement removes newline marks
            return re.findall("(?<=200.\s).{3,}[\s\S]*", form_filed)
        elif "FILING ID" in form_filed:
            # Currently, leaves in the id value, not sure how to regex it away
            return re.findall("(?<=FILING ID\s).{3,}[\s\S]*", form_filed)
        elif "DESCRIPTION:" in form_filed:
            # Currently, leaves in some stuff that isnt that important
            return re.findall("(?<=DESCRIPTION:\s).{3,}[\s\S]*", form_filed)
        elif "SUBHOLDING OF:" in form_filed:
            return re.findall("(?<=SUBHOLDING OF:\s).{3,}[\s\S]*", form_filed)
        elif "FILING STATUS: NEW" in form_filed:
            return re.findall("(?<=NEW\s).{3,}[\s\S]*", form_filed)
        return None
